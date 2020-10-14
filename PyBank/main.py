import os 
import csv 

#path to csvfile
filepath = os.path.join("PyBank","Resources","budget_data.csv")
#set variables 
total_months = 0
total_profit = 0
greatest_increase_month = 0
greatest_increase = 0
greatest_decrease_month = 0
greatest_decrease = 0
month_count = []
monthly_change = []

#open the csvfile
with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    row = next(csvreader)
    #find the total months, total profit gain/loss and set variables for rows in csv
    total_months += 1
    total_profit += int(row[1])
    greatest_increase_month = row[0]
    greatest_increase = int(row[1])
    greatest_decrease_month = row[0]
    greatest_decrease = int(row[1])
    previous_month_profit = int(row[1])
    #calculate total months and total profit gain/loss of entire dataset
    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])

        # calculate profit change from current month to previous month 
        profit_change = int(row[1]) - previous_month_profit
        monthly_change.append(profit_change)
        previous_month_profit = int(row[1])
        month_count.append(row[0])

        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    average_change = round(sum(monthly_change) / len(monthly_change),2)
    highest_profit = max(monthly_change)
    lowest_proft = min(monthly_change)

#print analysis
print(f"Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ( ${highest_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${lowest_proft})")

# create outputfile name 
outputfile = os.path.join("PyBank","Analysis.txt")
with open (outputfile,'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Financial Analaysis'])
    writer.writerow(["-------------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${total_profit}"])    
    writer.writerow([f"Average Change: ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_month} (${highest_profit}) "])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest_proft}) "])


        