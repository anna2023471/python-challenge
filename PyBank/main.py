import os
import csv

# Define file path
csvpath = os.path.join("Resources/budget_data.csv")

# Create list to append period totals to
totals = []

# Open and read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Define header of dataset
    csvheader = next(csvreader)
    # Define first row of dataset
    csvfirstrow = next(csvreader)
    # Define previous row variable
    previous_row = float(csvfirstrow[1])
    # Append first row column 2 value to list of period totals
    totals.append(float(csvfirstrow[1]))
    # Create list to append changes in column 2 values between periods to
    change_list = []
    # Set starting value for greatest positive difference between period totals
    greatest_increase = 0
    # Set variable to hold the period of the greatest positive difference
    greatest_increase_month = ""
    # Set starting value for greatest negative difference between period totals
    greatest_decrease = 0
    # Set variable to hold the period of the greatest negative difference
    greatest_decrease_month = ""

# Start looping through file
    for row in csvreader:
        # Append all values in column 2 to a list
        totals.append(float(row[1]))
        # Sum all values in list
        final_total = sum(totals)
        # Calculate difference between current and previous row for first and second rows
        net_change = float(row[1]) - previous_row
        # Change previous row to iterate through all rows in file (not just all rows less first row)
        previous_row = float(row[1])
        # Append calculated differences to a list
        change_list.append(float(net_change))
        # While iterating through list of differences, compare against present variable and find greatest positive value
        if net_change > greatest_increase:
            # Set greatest difference value as the greatest increase variable
            greatest_increase = net_change
            # Also return the relevan month for the greatest increase
            greatest_increase_month = row[0]
        # While iterating through list of differences, compare against present variable and find greatest negative value
        if net_change < greatest_decrease:
            # Set greatest difference value as the greatest decrease variable
            greatest_decrease = net_change
            # Also return the relevan month for the greatest decrease
            greatest_decrease_month = row[0]

    # Count number of values in the totals list
    length_totals = len(totals)
    # Count number of values in the between-period value changes list
    length_changes = len(change_list)
    # Calculate total of all between-period changes
    all_changes = sum(change_list)
    # Calculate the average between-period change
    average_change = all_changes / len(change_list)
        
# Print document heading
print("Financial Analysis")
# Print break
print("------------------------------")
# Print total time periods
print(f"Total Months: {len(totals)}")
# Print total of Profit/Losses
print(f"Total: {final_total:.0f}")
# Print average between-period change
print(f"Average Change: ${average_change:.2f}")
# Print the greatest positive change between periods with relevant month
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})")
# Print the greatest negative change between periods with relevant month
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:.0f})")

# Create text file
with open("Analysis/bank_results.txt", "w") as textfile:
# Write everything that was printed to the terminal above, with each entry starting on a new line, and with a space between each line, into the text file
    textfile.write("Financial Analysis\n")
    textfile.write("\n")
    textfile.write("------------------------------\n")
    textfile.write("\n")
    textfile.write(f"Total Months: {len(totals)}\n")
    textfile.write("\n")
    textfile.write(f"Total: {final_total:.0f}\n")
    textfile.write("\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})\n")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:.0f})\n")





                