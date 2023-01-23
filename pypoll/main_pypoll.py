# import dependicies
import os
import csv

# create path to csv file
budget_csv = os.path.join(".", "Resources", "election_data.csv")
# path to analysis
budget_report = os.path.join(".", "analysis", "election_report.txt")

total_votes = 0
canidates = []
canidate_votes = {}

# open the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   

    # Read header
    header = next(csvreader) 

    # get data from 1st row
    firstrow = next(csvreader)
    total_votes += 1

    for row in csvreader:
        # add all months
        total_votes += 1
        if row[2] not in canidates:
            canidates.append(row[2])
        
        if row[2] not in canidate_votes:
           canidate_votes[row[2]] = 0
        canidate_votes[row[2]] += 1
        


#print('canidate votes: ' + str(canidate_votes))
#print("canidates: " + str(canidates))

winner_votes = max(canidate_votes.values())  
winner = max(canidate_votes, key=canidate_votes.get)    
    
    
    
    
# create report
report = (
    f'Election Results\n'
    f'...........................\n'
    f'Total Votes : {total_votes}\n'
    f'Canidates: {canidate_votes}\n'
    f'Winner: {winner} {winner_votes}\n'
    

)
print(report)
# save report
with open(budget_report, 'w') as txtfile: 
    txtfile.write(report)