#TASK 
'''Printing a specified pattern'''

#SOLUTION 

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print each number 'i' repeated 'i' times
    for j in range(i):
        print(i, end=" ")
    
    # Move to the next line after each row
    print()