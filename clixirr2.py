import csv, datetime, financial

# see https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py

def get_dates(cashflows, balances, fun):
    results = []
    if cashflows:
        start_date = cashflows[0][0]
        start_balance = 0.0
        for txn in balances:
            cf = [t for t in cashflows if t[0] >= start_date and t[0] <= txn[0]]
            cf.append([start_date, start_balance])
            cf.append(txn)
            results.append([start_date, txn[0], fun(cf)])
            start_date = txn[0]
            start_balance = -txn[1]
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

        
    get_dates(cashflows, balances, financial.xirr)
    cashflows.append(balances[-1])
    print(financial.xirr(cashflows))


if __name__ == "__main__":
   main(['-isource'])    
