import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

total_votes = 0
candidates = []
candidate_votes_dict = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes_dict[candidate] = 0
        candidate_votes_dict[candidate] += 1

    print(total_votes)

with open("Analysis/poll_results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
                
    winning_vote = 0
    winner = ""

    for candidate in candidate_votes_dict:
        votes = candidate_votes_dict[candidate]
        percent_votes = votes / total_votes * 100
        print(f'{candidate} {percent_votes:.3f}% {votes}')
        textfile.write(f"{candidate} {percent_votes:.3f}% {votes}\n")
        if votes > winning_vote:
            winning_vote = votes
            winner = candidate
            
    print(f'Winner: {winner}')
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
    textfile.write(f'Winner: {winner}')
