import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")

totals = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    csvfirstrow = next(csvreader)

    previous_row = float(csvfirstrow[1])
    totals.append(float(csvfirstrow[1])) 
    change_list = []
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

    for row in csvreader:
        totals.append(float(row[1]))
        final_total = sum(totals)
        net_change = float(row[1]) - previous_row
        previous_row = float(row[1])
        change_list.append(float(net_change))
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

    length_totals = len(totals)
    length_changes = len(change_list)
    all_changes = sum(change_list)
    average_change = all_changes / len(change_list)
    print({len(change_list)})
    print({average_change})
    

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(totals)}")
print(f"Total: {final_total:.0f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:.0f})")
      
with open("Analysis/bank_results.txt", "w") as textfile:
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





                