import os
import csv

# make path for data pull
budget_data = os.path.join('..','Instructions','PyBank', 'Resources', 'budget_data.csv')

#initialize the variables
count = 0
total = 0
changes = 0

#create list to store the changes (differences) in profits/losses
changelist = []


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvreader)

    #set previous row
    firstrow=next(csvreader)
    previousnet = int(firstrow[1])
    total += int(firstrow[1])
    count += 1


    #count number of months, net profits/losses, average of the changes
    for row in csvreader:
        count += 1
        total += int(row[1])
        netchange = int(row[1])-previousnet
        changelist += [netchange]
        previousnet=int(row[1])

sumofchanges = sum(changelist)/len(changelist)

print('Financial Analysis')
print('-----------------------------')
print(f'Total Months: {count}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sumofchanges, 2)}')

