#TASK 
'''Iterate the given list of numbers and print only those numbers which are divisible by 5'''

#SOLUTION 
# Take list input from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of substrings
user_list_str = user_input.split()

# Convert each substring to an integer (removing commas if any)
user_list = [int(num.replace(',', '')) for num in user_list_str]

# Iterate through the list and print numbers divisible by 5
print("Numbers divisible by 5:")
for num in user_list:
    if num % 5 == 0:
        print(num)