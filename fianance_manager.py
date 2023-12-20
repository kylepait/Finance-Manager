import csv

FILE = 'file.csv'



def finance_manager(file):
    sum = 0
    transactions = []

    with open(file, mode='r') as csv_file:
        #read in file
        csv_reader = csv.reader(csv_file)

        #skip the header
        header = next(csv_reader)

        #loop over rows
        for row in csv_reader:
            #retrieve name, amount and currency
            #these indecies will change depending on how the
            #finanical institution you use exports to csv

            name = row[2]
            amount = float(row[6])
            date = row[0]

            transaction = (date, name, amount)
            sum += amount
            transactions.append(transaction)
            
    print(f"The sum of you transactions this month is {sum}")
    print('')
    return transactions

print(finance_manager(FILE))