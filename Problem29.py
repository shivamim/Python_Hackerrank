#TASK 
''' Count the total number of digits in a number'''

#SOLUTION 
number = int(input("Enter a number: "))

number_str = str(number)

digit_count = len(number_str)

print(f"The total number of digits in {number} is: {digit_count}")
