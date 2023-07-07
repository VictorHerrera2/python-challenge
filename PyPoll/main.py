import os
import csv
#CREATE VARIABLES AND LISTS------
total_votes = 0
candidate_list =[]
candidateVotes_list = []
candidataPercnt_list = []
complete_list =[]

charles = []
charles_total = 0
percent_charles = 0

diana =[]
diana_total = 0
percent_diana = 0

raymon = []
raymon_total = 0
percent_raymon = 0

charles_rate =[]
diana_rate = []
raymon_rate = []
candidate_rate =[]
# END-----------------------------
#CREATE PATH FOR FILE
csvpath = os.path.join('Resources','election_data.csv')
txtpath = os.path.join('Resources','election_data.txt')
#OPEN  FILE, READ AND TAKE CARE OF HEADER
with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)
    #ADD VALUES TO DESIRED LISTS 
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        elif row[2] == "Charles Casper Stockham":
            charles.append(row[2])
        elif row[2] == "Diana DeGette":
            diana.append(row[2])
        elif row[2] == "Raymon Anthony Doane":
            raymon.append(row[2])

    #FINDS TOTAL VOTES AND VOTES FOE EACH CANDIDATE
    total_votes = 3+len(charles)+len(diana)+len(raymon)
    charles_total = len(charles)+1
    diana_total = len(diana)+1
    raymon_total = len(raymon)+1
    #CALCUATE THE PERCENTS OF VOTES
    percent_charles = round((charles_total/total_votes)*100,3)
    charles_rate.append(str(percent_charles) + "%")
    percent_diana = round((diana_total/total_votes)*100,3)
    diana_rate.append(str(percent_diana) + "%")
    percent_raymon = round((raymon_total/total_votes)*100,3)
    raymon_rate.append(str(percent_raymon) + "%")
    #LIST OF TOTAL VOTES OF EACH CANDIDATE
    candidateVotes_list.append(charles_total)
    candidateVotes_list.append(diana_total)
    candidateVotes_list.append(raymon_total)
    #LIST OF PERCENTS 
    candidate_rate.append(charles_rate)
    candidate_rate.append(diana_rate)
    candidate_rate.append(raymon_rate)
    #GET RESULTS
    complete_list = list(zip(candidate_list,candidate_rate,candidateVotes_list))

    output = (f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes:,{total_votes}\n"
    f"----------------------------\n")
    print(output)
    for row in complete_list:
        print(row)
    #CALCULATE WINNER
    if (charles_total >= diana_total) and (charles_total >= raymon_total):
        largest = charles_total
        output_1 = f"Winner: Charles Casper Stockham"
        print(output_1)
    elif (diana_total >= charles_total) and (diana_total >= raymon_total):
        largest = diana_total
        output_1 = f"Winner: Diana DeGette"
        print(output_1)
    else:
        largest = raymon_total
        output_1 = f"Winner: Raymon Anthony Doane"
        print(output_1)
        print("-----------------------------")
    
    textWrite = str(complete_list)
# Open the file using "write" mode. Specify the variable to hold the contents
with open(txtpath, "w") as txt_file:
    txt_file.write(output)
    txt_file.write(textWrite+"\n")
    txt_file.write(output_1)



 

             

    

 

            



