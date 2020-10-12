import os 
import csv 

#path to csvfile
filepath = os.path.join("PyBank","Resources","budget_data.csv")
#set variables 
total_months = 0
net_total = 0
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
    # find total number of months,net total of profit/less and set variables for rows 
    total_months += 1
    net_total += int(row[1])
    # greatest_increase_month = row[0]
    # greatest_increase = int(row[1])
    # greatest_decrease_month = row[0]
    # greatest_increase = int(row[1])
    previous_month_profit = int(row[1])
    
    
    for row in csvreader:
        total_months += 1 
        net_total += int(row[1])

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
    high = max(monthly_change)
    low = min(monthly_change)

#print analysis
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, ( ${high})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${low})")

# create outputfile name 
outputfile = os.path.join("PyBank","Analysis.txt")
with open (outputfile,'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Financial Analaysis'])
    writer.writerow(["-------------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net_total}"])    
    writer.writerow([f"Average Change: ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_month} (${high}) "])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_month} (${low}) "])


        