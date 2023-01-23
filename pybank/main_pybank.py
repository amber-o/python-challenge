# import dependicies
import os
import csv

# create path to csv file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
# path to analysis
budget_report = os.path.join(".", "analysis", "budget_report.txt")

# Lists to store data
date = []
profit_losses = []
total_months = 0
total_profit = 0.0
differnce = []
first_r = 0
all_months = []
# open the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   

    # Read header
    header = next(csvreader) 

    # get data from 1st row
    firstrow = next(csvreader)
    total_months += 1
    total_profit += int(firstrow[1])
    first_r = int(firstrow[1])
    for row in csvreader:
        # add all months
        total_months += 1
        #add all profits
        total_profit += int(row[1])  
        
        diff = int(row[1])  - first_r 
        first_r = int(row[1])
        differnce.append(diff)

        all_months.append(row[0])
        
    length = len(differnce)
    # print('length: ' + str(length))
    sum = sum(differnce)
    # print('sum: ' + str(sum))
    average = sum/length
    # print('average:' + str(average))

    max_change = max(differnce)
    max_index = differnce.index(max_change)
    # print('max: '+ str(max_change))
    # print('max month: ' + all_months[max_index])
    min_change = min(differnce)
    min_index = differnce.index(min_change)


        


       
    # print(differnce)
    # print(total_months)
    # print(total_profit)     

    
    
    


# create report
report = (
    f'Financial Analysis\n'
    f'................................\n'
    f'Total Months: {total_months}\n'
    f'Total: {total_profit}\n'
    f'Average Change: {average}\n'
    f'Greatest Increase in Profits: {all_months[max_index]} {max_change}\n'
    f'Greatest Decrease in Profits: {all_months[min_index]} {min_change}\n'

)
print(report)
# save report
with open(budget_report, 'w') as txtfile: 
    txtfile.write(report)