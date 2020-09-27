#Imports
import os
import csv
import sys
#loadCSV
pybankcsv = os.path.join('Resources','budget_data.csv')

#readCSV
with open(pybankcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)

    #Set base variables
    totalmo = 0
    totalpro = 0
    avgchg = 0
    pandl = []
    change = 0
    prevvalue = 0
    giip = 0
    gdip = 0

    #startfunction
    for rows in csvreader:
        totalmo = totalmo + 1 #counting total months
        totalpro = totalpro + int(rows[1]) #counting total profit/loss
        change = int(rows[1]) - prevvalue #calculate P/L by taking the current row from the previous
        prevvalue = int(rows[1]) #now that we have our change for this row, store the current row's P/L as the previous value
        pandl.append(change) #add the change value to the pandl list

        #larger than previous greatest
        if (change > giip):
            giipmo = rows[0] #store date
            giip = change #store value
        #smaller than previous smallest
        if (change < gdip):
            gdipmo = rows[0] #store date
            gdip = change #store value

    avchange = (sum(pandl)) / totalmo #calculate average change


    #print results
    print("\n--------------------- \n Financial Analysis \n---------------------")
    print(f"Total Months: {totalmo}")
    print(f"Total: ${totalpro}")
    print(f"Average Change: ${avchange}")
    print(f"Greatest Increase in Profits: {giipmo} (${giip})")
    print(f"Greatest Decrease in Profits: {gdipmo} (${gdip}) \n---------------------")

    #write CSV
    output_path = os.path.join('analysis', 'FinAna.txt')

    #open file in write mode
    sys.stdout = open(output_path, "w")
    print("\n--------------------- \n Financial Analysis \n---------------------")
    print(f"Total Months: {totalmo}")
    print(f"Total: ${totalpro}")
    print(f"Average Change: ${avchange}")
    print(f"Greatest Increase in Profits: {giipmo} (${giip})")
    print(f"Greatest Decrease in Profits: {gdipmo} (${gdip}) \n---------------------")
    sys.stdout.close()


        