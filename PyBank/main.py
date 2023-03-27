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
        

