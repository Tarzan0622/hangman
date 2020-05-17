import csv
with open("投資計画2019.xlsx","r", encoding="utf-8") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
       print(",".join(row))