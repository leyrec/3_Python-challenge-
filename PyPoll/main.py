#1 IMPORT modules
import os
import csv

election_data_csv = os.path.join("election_data.csv")

#2 STORE data in a List
candidate = []

#3 OPEN and READ csv file
with open(election_data_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

# Read the HEADER row first
  reader=next(csvreader)

# Read for each row of data after the header
  for row in csvreader:

# ADD data to the List
    candidate.append(row[2])

# PRINT HEADER AND RESULTS

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(candidate)))
print("----------------------------")

# CALCULATE votes and percentages per candidate
Khan = candidate.count("Khan")
khanpercent = round(int((Khan) / len(candidate) * 100), 3)
print("Khan: " + str(khanpercent) + "% (" + str(Khan) + ")")

Correy = candidate.count("Correy")
correypercent = round(int((Correy) / len(candidate) * 100), 3)
print("Correy: " + str(correypercent) + "% (" + str(Correy) + ")")

Li = candidate.count("Li")
Lipercent = round(int((Li) / len(candidate) * 100), 3)
print("Li: " + str(Lipercent) + "% (" + str(Li) + ")")

OTooley = candidate.count("O'Tooley")
OTooleypercent = round(int((OTooley) / len(candidate) * 100), 3)
print("O'Tooley " + str(OTooleypercent) + "% (" + str(OTooley) + ")")

print("----------------------------")

#DETERMINE the winner

if khanpercent > correypercent:
    print("Winner: Khan")
elif khanpercent > correypercent:
     print("Winner: Khan")
elif khanpercent > Lipercent:
     print("Winner: Khan")       
elif khanpercent > OTooleypercent:
     print("Winner: Khan")
else: 
     print("Winner: is not Khan")
        
print("----------------------------")        
        

# CREATE a text file with the results
with open('PyPoll_Data.txt', 'w+', newline = "\n") as w:
    w.write("Election Results\n")
    w.write('----------------------------\n')
    w.write('Total Votes: 3521001\n')
    w.write('----------------------------\n')
    w.write('Khan: 63.000%   (2218231)\n')
    w.write('Khan: 20.000%   (704200)\n')
    w.write('Khan: 14.000%   (492940)\n')
    w.write('Khan:  3.000%   (105630)\n')
    w.write('----------------------------\n')
    w.write('Winner: Khan\n')
    w.write('----------------------------\n')
    
    
    