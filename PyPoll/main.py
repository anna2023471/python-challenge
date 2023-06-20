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
        # For each row, add a count of 1 to the votes variable
        total_votes = total_votes + 1
        # Look for candidate for the candidates list in column 3
        candidate = row[2]
        # If the name in the row isn't currently in the candidates list, add it to the candidates list
        if candidate not in candidates:
            candidates.append(candidate)
            # Set the dictionary index to 0 for first candidate
            candidate_votes_dict[candidate] = 0
        # Add 1 to the index of previous candidate to create the dictionary index for new candidate
        candidate_votes_dict[candidate] += 1

    # Print document heading
    print("Election Results")
    # Print break
    print("-------------------------")
    # Print the total number of votes in dataset to the terminal
    print(total_votes)
    # Print break
    print("-------------------------")

# Create text file
with open("Analysis/poll_results.txt", "w") as textfile:
    # Write everyting that was printed to the terminal above, with each entry starting on a new line, with a space between each line, to the text file
    textfile.write("Election Results\n")
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
                
    # Set the initial value for the winning vote count
    winning_vote = 0
    # Set variable to hold the winner's name
    winner = ""

    # Start iterating through the candidates in the candidate dictionary
    for candidate in candidate_votes_dict:
        # Allocate votes to each candidate in the dictionary
        votes = candidate_votes_dict[candidate]
        # Calculate votes allocated to each candidate as percentage of total votes
        percent_votes = votes / total_votes * 100
        # Print the candidate's name, with percentage of votes receives, and count of votes received by that candidate
        print(f'{candidate}: {percent_votes:.3f}% ({votes})')
        # Write what was printed to the terminal above to the text file
        textfile.write(f"{candidate}: {percent_votes:.3f}% ({votes})\n\n")
        # Compare each candidates votes to the original value set, and find the highest count
        if votes > winning_vote:
            # Set the winning vote to equal to the highest candidate vote coung
            winning_vote = votes
            # Set the winner to be the candidate name with the highest vote count
            winner = candidate
            
    # Print the winner's name 
    print(f'Winner: {winner}')
    # Write the winners name, with spaces and a break, to the text file.
    textfile.write("\n")
    textfile.write("--------------------------\n")
    textfile.write("\n")
    textfile.write(f'Winner: {winner}')
