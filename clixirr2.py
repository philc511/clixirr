import csv, datetime, financial, sys

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
            answer = fun(cf)
            if (answer != answer):
                print("NAN ALERT for this input array:")
                print(cf)
            results.append([start_date, end_date, answer])
            start_date = end_date
    return results

def get_dated_items(filename):
    items = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(filter(lambda row: row[0]!='#', csvfile), delimiter=',')
        for row in spamreader:
            txn_date = datetime.datetime.fromisoformat(row[0])
            amount = float(row[1])
            items.append([txn_date, amount])
    # todo sort these
    return items

def get_date_string(d):
    return d.strftime("%b-%Y")

def main(txn_file, balance_file):
    cashflows = get_dated_items(txn_file)
    balances = get_dated_items(balance_file)
        
    results = get_dates(cashflows, balances, financial.xirr)
    for r in results:
        print(get_date_string(r[0]), ",", get_date_string(r[1]), ",", format(r[2], ".1%"))
    cashflows.append(balances[-1])
    print(get_date_string(results[0][0]), ",", get_date_string(results[-1][1]), ",", format(financial.xirr(cashflows), ".1%"))


if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])    
