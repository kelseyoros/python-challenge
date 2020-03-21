import os
import csv

# make path for data pull
budget_data = os.path.join('..','Python-Challenge','Resources', 'budget_data.csv')

#initialize the variables
count = 0
total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

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
        previousnet = int(row[1])

        if netchange > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1] = netchange
        
        if netchange < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1] = netchange

sumofchanges = sum(changelist)/len(changelist)

print('Financial Analysis')
print('-----------------------------')
print(f'Total Months: {count}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sumofchanges, 2)}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')


write_to_file = (
'Financial Analysis\n'
'-----------------------------\n'
f'Total Months: {count}\n'
f'Total: ${total}\n'
f'Average Change: ${round(sumofchanges, 2)}\n'
f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')


#set the variable for the output file
output_file = os.path.join('Resources', 'budget_data_final.txt')

with open(output_file,"w") as datafile:
    datafile.write(write_to_file)