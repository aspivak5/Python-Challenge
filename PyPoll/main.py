import os
import csv
#path to csvfile 
filepath = os.path.join("PyPoll", "Resources", "election_data.csv")

#set variables 
total_votes = 0 
correy_votes = 0
khan_votes = 0
li_votes = 0
otooley_votes = 0

#open csvfile 
with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1

        #calcualte the total votes won for each candidate 
        if row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Li":
            li_votes += 1 
        else:
            otooley_votes += 1
    #calculate percantage of votes for each candidate 
    correy_percentage = round((correy_votes/total_votes) * 100,1)
    khan_percentage = round((khan_votes/total_votes) * 100,1)
    li_percentage = round((li_votes/total_votes) * 100,1)
    otooley_percentage = round((otooley_votes/total_votes) * 100,1)

    # find out who got the most votes
    most_votes = max(correy_votes, khan_votes, li_votes, otooley_votes)

    # based on who got most votes find the winner 

    if most_votes == correy_votes:
        winner = "Correy"
    elif most_votes == khan_votes:
        winner = "Khan"
    elif most_votes == li_votes:
        winner = "Li"
    else:
        winner = "O'tooley"

#print in terminal
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
print(f"Correy: {correy_percentage:.3f}% ({correy_votes})")
print(f"Khan: {khan_percentage:.3f}% ({khan_votes})")
print(f"Li: {li_percentage:.3f}% ({li_votes})")
print(f"O'tooley: {otooley_percentage:.3f}% ({otooley_votes})")
print("---------------------------------")
print(f"WINNER: {winner}")

# create outputfile name 
outputfile = os.path.join("PyPoll","Analysis.txt")
with open (outputfile,'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["---------------------------------"])
    writer.writerow([f"Correy: {correy_percentage:.3f}% ({correy_votes})"])
    writer.writerow([f"Khan: {khan_percentage:.3f}% ({khan_votes})"])
    writer.writerow([f"Li: {li_percentage:.3f}% ({li_votes})"])
    writer.writerow([f"O'tooley: {otooley_percentage:.3f}% ({otooley_votes})"])
    writer.writerow(["---------------------------------"])
    writer.writerow([f"WINNER: {winner}"])
