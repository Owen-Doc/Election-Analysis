# The data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3 . The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote
#NOTE: You should be working from the Mod3 directory in terminal!
# import datetime as dt
# now = dt.datetime.now()
# print('The time right now is ', now)
# import csv
# #dir(csv)
# # Use this method if you know the direct path
# # file_to_load = 'Resources/election_results.csv'
# # # Open the election results and read the file
# # 

# import os
#Use this method if you do not know the file path - this will join them into a path


#Add dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file
with open(file_to_load) as election_data:
    # To do, read and analyze data here
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    
    










