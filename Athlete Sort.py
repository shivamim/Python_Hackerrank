#TASK
'''You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight, and so on). 
You are required to sort the data based on the Kth attribute and print the final resulting table.
Note that K is indexed from 0 to (M-1), where M  is the number of attributes.

Constraints
1 <= N, M <= 1000
0 <= K < M'''

#SOLUTION 
def athlete_sort():
    # initiailzing map function
    N, M = map(int, input().split())

    # taking for rows
    rows = [input() for _ in range(N)]

    # taking input from user
    K = int(input())


    # sorting using sorted function
    for row in sorted(rows, key=lambda row: int(row.split()[K])):
        print(row)
    
# Calling the function
athlete_sort()
