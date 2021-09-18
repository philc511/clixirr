import csv

class Transaction:
    def __init__(self, txn_date, txn_amount, balance):
        self.txn_date = txn_date
        self.txn_amount = txn_amount
        self.balance = balance

    def __str__(self):
        return self.balance


def main(argv):
    txns = []
    with open('txns.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(': '.join(row))
            txns.append(Transaction(row[0], row[1], row[2]))
    
    print(str(txns[0]))


if __name__ == "__main__":
   main(['-isource'])    