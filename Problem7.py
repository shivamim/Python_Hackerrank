#TASK 
'''Return the count of a given substring from a string'''

#SOLUTION 

str= input('Enter Your String:')
# Get substring to count
substring = input("Enter the substring to count: ")

# Initialize a variable to store the count
count = 0

# Iterate through the string
for i in range(len(str) - len(substring) + 1):
    # Check if the substring matches the current slice of the string
    if str[i:i+len(substring)] == substring:
        count += 1

# Print the count
print("Count of '{}' in the string: {}".format(substring, count))