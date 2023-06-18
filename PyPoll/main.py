import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

all_votes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        all_votes.append(row[1])
        number_of_votes = len(all_votes)
        
print(len(all_votes))




