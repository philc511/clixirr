import csv, datetime, financial

class Transaction:
    def __init__(self, txn_date, txn_amount, balance):
        self.txn_date = datetime.datetime.fromisoformat(txn_date)
        self.txn_amount = float(txn_amount)
        self.balance = float(balance)

    def __str__(self):
        return self.balance
    
    def get_cashflow(self):
        amount = self.txn_amount
        if (amount == 0.0):
            amount = self.balance
        return [self.txn_date, amount]
        

# see https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py

def get_dates(txns):
    dates = []
    start_date = txns[0].txn_date
    for txn in txns:
        if txn.txn_amount == 0.0:
            dates.append([start_date, txn.txn_date])
            start_date = txn.txn_date
    return dates

def xirr(txns):
    for txn in txns:
        print(str(txn))
    cashflows=[]
    for txn in txns:
        if txn.txn_amount != 0.0:
            cashflows.append(txn.get_cashflow())
    cashflows.append(next(i for i in reversed(txns) if i.txn_amount == 0.0).get_cashflow())
    #print(cashflows)
    return financial.xirr(cashflows)

def main(argv):
    txns = []
    with open('txns.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            #print(': '.join(row))
            txns.append(Transaction(row[0], row[1], row[2]))
    
    dates = get_dates(txns)
    print(xirr(txns))
    for pair in dates:
        print(xirr([t for t in txns if t.txn_date >= pair[0] and t.txn_date <= pair[1]]))


if __name__ == "__main__":
   main(['-isource'])    