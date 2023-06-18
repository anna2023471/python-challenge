import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")

totals = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        totals.append(float(row[1]))
        final_total = sum(totals)
    
length_totals = len(totals)
print(f"Total Months: {len(totals)}")
print(f"Total: {final_total}")
print(f"{totals.index(float(row[1]))}")

# totals = []
# change_list = []

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csvheader = next(csvreader)  

#     for row in csvreader:
#         totals.index(float(row[1]))
print(f'{totals.index(float(row[1]))}')


    

#         change = (totals.index(float(row[1]))) - (totals.index(float(row[1])))
#         change_list = change_list.append(change)
        
# total_change = sum(change_list)
# length_total_change = len(change_list)
# average_total_change = total_change / len(change_list)
# print(average_total_change)





                