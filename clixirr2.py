import csv, datetime, financial

# see https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py

def get_dates(cashflows, balances, fun):
    results = []
    if cashflows and len(set([b[0] for b in balances] + [c[0] for c in cashflows])) > 1:
        start_date = cashflows[0][0]
        end_dates = list(set([b[0] for b in balances]))
        end_dates.sort()

        for end_date in end_dates:
            cf = [t for t in cashflows if t[0] >= start_date and t[0] <= end_date]
            # add all balances on start date (but negated)
            cf.extend([[b[0], -b[1]] for b in balances if b[0] == start_date])
            # add all balances on end date
            cf.extend([b for b in balances if b[0] == end_date])
            results.append([start_date, end_date, fun(cf)])
            start_date = end_date
    return results

def main(argv):
    txns = []
    cashflows = []
    balances = []
    with open('txns.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            #print(': '.join(row))
            txn_date = datetime.datetime.fromisoformat(row[0])
            amount = float(row[1])
            balance = float(row[2])
            if amount != 0.0:
                cashflows.append([txn_date, amount])
            else:
                balances.append([txn_date, balance])

        
    print(get_dates(cashflows, balances, financial.xirr))
    cashflows.append(balances[-1])
    print(financial.xirr(cashflows))


if __name__ == "__main__":
   main(['-isource'])    
