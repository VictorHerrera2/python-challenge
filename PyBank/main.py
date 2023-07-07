
import os
import csv

#CREATE DESIRED VARIABLES AND LISTS
total_months = 0
list = []
diff_list = []
net_total = 0
great_incr = 0
great_decr = 0
avg_change = 0
date = []
#CREATE PATH FOR FILE
csvpath = os.path.join('Resources','budget_data.csv')
txtpath = os.path.join('Resources','budget_data.txt')
#OPEN  FILE, READ AND TAKE CARE OF HEADER
with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)
   
    #FIND THE NET & MONTH TOTAL
    for row in csvreader:
        list.append(int(row[1]))  
        date.append(row[0])
    date.remove('Jan-10') 
    #CALCULATE AND STORE RESULTS IN VARIABLES OR LISTS  
    total_months = len(list)
    net_total = sum(list)
    diff_list = [list[i+1]-list[i] for i in range (len(list)-1)]
    avg_change = (sum(diff_list))/len(diff_list)
    great_incr = max(diff_list)
    great_decr = min(diff_list)
    f_dictionary = dict(zip(diff_list,date))
    incr_date = f_dictionary[great_incr]
    decr_date = f_dictionary[great_decr]
    #PRINT THE DEISRED RESULTS
    output = (f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months:,{total_months}\n"
    f"Total: $,{net_total}\n"
    f"Average Change: $,{avg_change}\n"
    f"Greatest Increase in Profits:,{incr_date},{great_incr}\n"
    f"Greatest Decrease in Profits:,{decr_date},{great_decr}\n" )
    print(output)
with open(txtpath, "w") as txt_file:
    txt_file.write(output)

    



    
    
    
   

   
        
        
    
    






    
      



