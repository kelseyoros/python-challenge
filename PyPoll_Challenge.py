import os
import csv

#make path for data pull
election_data = os.path.join('..','Python-Challenge','Resources', 'election_data.csv')

#Initialize variables
count = 0
winner_votes = 0

#Set empty lists, dictionaries, and variables
candidate_options = [] 
candidate_votes = {}
winner = ""


with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1
        candidatename=row[2]

        # traverse for all elements 
        if candidatename not in candidate_options:
            candidate_options.append(candidatename)

            candidate_votes[candidatename] = 0

        candidate_votes[candidatename] +=1

#Find winner
for candidatename, votecount in candidate_votes.items():
    if votecount > winner_votes:
        winner_votes = votecount
        winner = candidatename


print("Election Results")
print('-----------------------------')
print(f'Total Votes: {count}')
print('-----------------------------')
# Iterate over key/value pairs in dict and print them
for key in candidate_votes:
    print(f'{key}: {round(candidate_votes[key]/count*100, 3)}%  ({candidate_votes[key]})')
print('-----------------------------')
print(f'Winner: {winner}')
print('-----------------------------')


#set the variable for the output file
output_file = os.path.join('Resources', 'election_data_final.txt')

with open(output_file,"w") as datafile:
    datafile.write('Election Results\n'
    '-----------------------------\n'
    f'Total Votes: {count}\n'
    '-----------------------------\n')
    for key in candidate_votes:
        datafile.write(f'{key}: {round(candidate_votes[key]/count*100, 3)}%  ({candidate_votes[key]})\n')
    datafile.write('-----------------------------\n'
    f'Winner: {winner}\n'
    '-----------------------------\n')