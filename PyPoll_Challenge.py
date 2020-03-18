import os
import csv

# make path for data pull
election_data = os.path.join('..','Python-Challenge','Resources', 'election_data.csv')

#Initialize variables
count = 0

candidate_list = [] 

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1

    def unique(candidates): 
        candidates = row[2]
        # Create empty list to store 

      
        # traverse for all elements 
        for x in candidates: 
        # check if exists in unique_list or not 
            if x not in candidate_list: 
                candidate_list.append(x)
                
                    
    print("Election Results")
    print('-----------------------------')
    print(f'Total Votes: {count}')
    print('-----------------------------')
    print(f'{unique}')