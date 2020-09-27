#imports
import os
import csv
import sys

#loadcsv
pypollcsv = os.path.join('Resources','election_data.csv')

#readcsv
with open(pypollcsv, 'r') as csvfile:
    pypoll = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)

    #set base variables
    votetotal = 0
    candidates = ["Khan","Correy","Li","O'Tooley"]
    khanper = 0
    khantotal = 0
    correyper = 0
    correytotal = 0
    liper = 0
    litotal = 0
    otoolper = 0
    otooltotal = 0

    #start function
    for rows in pypoll:
        votetotal = votetotal + 1 #count number of votes
        if rows[2] == "Khan":
            khantotal = khantotal+1 #tally Khan total vote
        elif rows[2] == "Correy": 
            correytotal = correytotal+1 #tally Correy total vote
        elif rows[2] == "Li":
            litotal = litotal+1 #tally Li total vote
        elif rows[2] == "O'Tooley":
            otooltotal = otooltotal+1 #tally O'tooley total vote

    #determine percentage of vote
    khanper = khantotal / votetotal
    khanclean = "{:.3%}".format(khanper)
    correyper = correytotal / votetotal
    correyclean = "{:.3%}".format(correyper)
    liper = litotal / votetotal
    liclean = "{:.3%}".format(liper)
    otoolper = otooltotal / votetotal
    otoolclean = "{:.3%}".format(otoolper)

    #determine winner
    if khanper > correyper and liper and otoolper:
        winner = "Khan"
    elif correyper > khanper and liper and otoolper:
        winner = "Correy"
    elif liper > khanper and correyper and otoolper:
        winner = "Li"
    elif otoolper > khanper and correyper and liper:
        winner = "O'Tooley"

    #print results

    print("---------------------\n Election Results \n---------------------")
    print(f"Total Votes: {votetotal}\n---------------------")
    print(f"Khan: {khanclean} ({khantotal})")
    print(f"Correy: {correyclean} ({correytotal})")
    print(f"Li: {liclean} ({litotal})")
    print(f"O'Tooley: {otoolclean} ({otooltotal})")
    print(f"---------------------\n Winner: {winner}\n---------------------" )

    #write CSV
    output_path = os.path.join('analysis', 'electionresults.txt')

    #open file in write mode
    sys.stdout = open(output_path, "w")
    print("---------------------\n Election Results \n---------------------")
    print(f"Total Votes: {votetotal} \n---------------------")
    print(f"Khan: {khanclean} ({khantotal})")
    print(f"Correy: {correyclean} ({correytotal})")
    print(f"Li: {liclean} ({litotal})")
    print(f"O'Tooley: {otoolclean} ({otooltotal})")
    print(f"---------------------\n Winner: {winner} \n---------------------" )
    sys.stdout.close()