import os
import csv

# Define file path
csvpath = os.path.join("Resources/election_data.csv")

# Set initial value for total vote count in dataset
total_votes = 0
# Create list to append candidate names to
candidates = []
# Create dictionary to hold candidate names and votes received by each candidate
candidate_votes_dict = {}

# Open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Define header of dataset
    csvheader = next(csvreader)

    for row in csvreader:
        # For each row, add a count of 1 to the total votes count
        total_votes = total_votes + 1
        # Look for candidate for the candidates list in column 3
        candidate = row[2]
        # If the name in the row isn't currently in the candidates list, add it to the candidates list
        if candidate not in candidates:
            candidates.append(candidate)
            # Set the initial count of votes for candidate to 0
            candidate_votes_dict[candidate] = 0
        # Add 1 to the count of votes for candidate
        candidate_votes_dict[candidate] += 1


with open("Analysis/poll_results.txt", "w") as textfile:
    # Print document heading
    print("Election Results\n\n")
    # Print break
    print("-------------------------\n\n")
    # Print the total number of votes in dataset to the terminal
    print(f'Total Votes: {total_votes}\n\n')
    # Print break
    print("-------------------------\n\n")

# Create text file
with open("Analysis/poll_results.txt", "w") as textfile:
    # Write everyting that was printed to the terminal above to the text file
    textfile.write("Election Results\n\n")
    textfile.write("--------------------------\n\n")
    textfile.write(f"Total Votes: {total_votes}\n\n")
    textfile.write("--------------------------\n\n")
                
    # Set the initial value for the winning vote count
    winning_vote = 0
    # Set variable to hold the winner's name
    winner = ""

    # Start iterating through the candidates in the candidate dictionary
    for candidate in candidate_votes_dict:
        # Set the votes variable to equal the count of votes for each candidate
        votes = candidate_votes_dict[candidate]
        # Calculate votes allocated to each candidate as percentage of total votes
        percent_votes = votes / total_votes * 100
        # Print the candidate's name, with percentage of votes received, and count of votes received by that candidate
        print(f'{candidate}: {percent_votes:.3f}% ({votes})\n\n')
        # Write what was printed to the terminal above to the text file
        textfile.write(f'{candidate}: {percent_votes:.3f}% ({votes})\n\n')
        # Compare each candidate's votes to the original value set, and find the highest count
        if votes > winning_vote:
            # Set the winning vote to equal the highest candidate vote count
            winning_vote = votes
            # Set the winner to be the candidate name with the highest vote count
            winner = candidate
            
    
    print("--------------------------\n\n")
    # Print the winner's name 
    print(f'Winner: {winner}\n\n')
    # Write the winners name to the text file.
    textfile.write("--------------------------\n\n")
    textfile.write(f'Winner: {winner}')
