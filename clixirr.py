import csv, datetime

class Transaction:
    def __init__(self, txn_date, txn_amount, balance):
        self.txn_date = datetime.datetime.fromisoformat(txn_date)
        self.txn_amount = float(txn_amount)
        self.balance = float(balance)

    def __str__(self):
        return self.balance

# see https://github.com/peliot/XIRR-and-XNPV/blob/master/financial.py
def secant_method(tol, f, x0):
    x1 = x0*1.1
    while (abs(x1-x0)/abs(x1) > tol):
        x0, x1 = x1, x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    return x1

def xnpv(rate,cashflows):
    chron_order = sorted(cashflows, key = lambda x: x[0])
    t0 = chron_order[0][0] #t0 is the date of the first cash flow

    return sum([cf/(1+rate)**((t-t0).days/365.0) for (t,cf) in chron_order])

def xirr(cashflows,guess=0.1):    
    return secant_method(0.0001,lambda r: xnpv(r,cashflows),guess)
    #return optimize.newton(lambda r: xnpv(r,cashflows),guess)

def xirr(txns):
    sum = 0
    for txn in txns:
        sum += txn.txn_amount
    return sum

def main(argv):
    txns = []
    with open('txns.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(': '.join(row))
            txns.append(Transaction(row[0], row[1], row[2]))
    
    print(xirr(txns))


if __name__ == "__main__":
   main(['-isource'])    