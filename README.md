# Election-Analysis
### An Audit Report of a Colorado Election
## Overview
One of the principles of democracy is a country's execution and verification of free and fair elections. Election audits are critical to ensure that every vote was counted, and that results are transparent and accurate. Colorado's Election Commission required an audit of their election results. I wrote a program in Python to draw from a CSV file that contains the results of a recent election in Colorado. The final program outputs the overall winner, total votes cast, each candidate's votes in count and percentage, and shows the largest county by total votes. In the data file, each voter has a unique, anonymous, Voter ID, their county, and the candidate that they voted for. To analyze this information, I use repitition statements, create lists, dictionaries, and conditional checks to create dynamic string outputs in a text file, so that the Election Commission can quickly view the results of my analysis. 

## Election-Audit Results

* There were 369,711 votes cast in this election
* Jefferson county accounted for 10.5% of the total vote with 38,855 votes
* Denver county accounted for 82.8% of the vote with 306,055 votes.
* Arapahoe county had 6.7% of the vote with 24,801 votes.
* Denver had the highest number of votes with 306,055 votes.
* There were 3 candidates in this election
  * Charles Casper Stockham: 23.0% (85,213 votes)
  * Diana DeGette: 73.8% (272,892 votes)
  * Raymon Anthony Doane: 3.1% (11,606)
* **Diana DeGette is the winner of the election with 272,892 votes, which was 73.8% of the vote**

## Election Audit Summary
The election commission has asked for some summary of how this code can be used in any election. 

First, I would have to verify the data file before applying my program. I'd need to verify column headers and data types match the structure of the file that I wrote this program for initially. Since I used a dictionary to hold the candidate name and votes in a key:value pair, if there were more than 3 candidates this code should still work as intended. 

One modification that I might make is if the election was extremely close, I would change some of my conditional checks to be "Greater than or equal to" instead of just greater than. In the event of a tie, my program would not accurately compute the overall winner. This can be seen in this block of code:
'''
if county_vote > winning_county_voters and county_vote_percent > winning_percentage:
            largest_county_name = county_name
            winning_county_voters = county_vote
'''
I also note that my program does not use any "50%" rule to determine the winner - which makes it useful for an election with multiple candidates. It only compares the total votes between all candidates and determines that the highest number of votes is the winner. In an election with a possible plurality, where no one achieves over 50% of the vote, this is a useful feature. However, I do note that there are some modifications I would make if there were, say 10 candidates in an election.

On my output page, I list the candidate's performance in no specific order other than how the datasheet is organized. In an election with 10 candidates, it may be useful to first include a section of the vote share of the top 3 candidates - that is who we would be most interested in to see first. Especially considering that it may be confusing/appear busy to have 10 rows of unsorted performance. I would likely use a nested for loop as the program goes through each candidate, and then use another conditional check to establish who the top 3 candidates are, and then use their name, vote count, and percentage to publish a separate section. This would give the reader a clear, concise snapshot of the top 3 performers, instead of having to look through a list of 10 candidates who may have received fractional shares of the vote.

