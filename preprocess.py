import csv
from decimal import Decimal # We don't want rounding errors.

newcsv = open("processed_data.csv", 'w', newline='')
newwriter = csv.writer(newcsv)
newwriter.writerow(["sales", "date", "region"])
for i in range(3):
    with open(f"data/daily_sales_data_{i}.csv", 'r', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row[0] == "pink morsel":
                sales = Decimal(row[1][1::]) * Decimal(row[2])
                newwriter.writerow([sales, row[3], row[4]])
