import csv

with open("lemma_result.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
