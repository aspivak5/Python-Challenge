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
changes = []

#open the csvfile
with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    
    
    for row in csvreader:
        print(row)