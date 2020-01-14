import csv


with open('ppl.csv', mode='r') as f1:
    reader = csv.reader(f1)
    next(reader)
    dic = dict((rows[0],tuple(rows[1:])) for rows in reader)
    print(dic)
