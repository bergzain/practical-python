# pcost.py
#
# Exercise 1.27
import csv,sys

def portfolio_cost(filename):
    # Your code here
    purchase_all=0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(f)
    for row in rows:
        # row = rows.split(',')
        shares = int(row[1])
        price = float(row[2])
        purchase = shares*price  
        purchase_all += purchase
    return purchase_all
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)


