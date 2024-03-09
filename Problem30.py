#TASK
'''Write a program to print the following start pattern using the for loop'''

#SOLUTION

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Print the upper part of the pattern
for i in range(1, num_rows + 1):
    print("* " * i)

# Print the lower part of the pattern
for i in range(num_rows - 1, 0, -1):
    print("* " * i)
