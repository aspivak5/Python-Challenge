import os 
import csv 

filepath = os.path.join("PyBank","Resources","budget_data.csv")
#set variables 
total_profit = 0
greatest_increase_month = 0
greatest_increase = 0
greatest_decrease_month = 0
greatest_decrease = 0
month_count = []
month_change = []
previous_month_profit = 0
profit_change=0

with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
#calculate total profit & months 
    for row in csvreader:
        total_profit += int(row[1])
        month_count.append(row[0])
        total_months=len(month_count)

        # Calculate change in profit 
        profit_change = int(row[1])- previous_month_profit 
        month_change.append(profit_change)
        previous_month_profit = int(row[1])
#find greatest increase and decrease 
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]   
        highest_profit = max(month_change)
        lowest_proft = min(month_change)
#remove first number in month change list and calculate average change
month_change.remove(867884)
average_change = round(sum(month_change) / len(month_change),2) 
#print analysis
print("Financial Analysis")
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