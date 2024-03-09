#TASK 
'''Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690'''

#SOLUTION 

# Take input from the user for the number of terms
n = int(input("Enter the number of terms (n): "))

# Initialize variables
term = int(input('Enter term:'))  # The first term in the series
sum_of_series = 0

# Loop to calculate and sum the series
for i in range(1, n + 1):
    # Calculate the current term by repeating '2' i times and converting to an integer
    current_term = int(str(term) * i)
    
    # Add the current term to the sum_of_series
    sum_of_series += current_term

# Print the sum of the series
print("Sum of the series:", sum_of_series)
