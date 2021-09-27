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
        if amount == 0.0:
            amount = self.balance
        return [self.txn_date, amount]
        

# see https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py

def xirr(txns):
    cashflows=[]
    for txn in txns:
        cashflows.append(txn.get_cashflow())
    return financial.xirr(cashflows)

def main(argv):
    txns = []
    with open('txns.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            #print(': '.join(row))
            txns.append(Transaction(row[0], row[1], row[2]))
    
    print(xirr(txns))


if __name__ == "__main__":
   main(['-isource'])    