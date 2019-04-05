import csv

with open('csv/data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)