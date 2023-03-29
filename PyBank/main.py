import csv
import os 

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

with open(csvpath, 'r') as csvfile:
    

    csvreader = csv.reader(csvfile, delimiter=",")
    
    print(csvreader)

    csv_header = next(csvreader)

    print("Header row:" + str(csv_header))

    for row in csvreader:
        print(row)
     
total_months = []
total_profits = []
profit_changes = 0
monthly_changes =0
previous_value = 0  
   
   
   
print("Financial Analysis")
print("----------------------------------")

total_months.append(row[0])
total_profits.append(row[1])









        

