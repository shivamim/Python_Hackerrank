#TASK 
''' Format variables using a string.format() method.'''

#SOLUTION 

totalMoney = 1000
quantity = 3
price = 450

# Using f-string (available in Python 3.6 and later)
formatted_string_f_string = f"Total money: ${totalMoney}, Quantity: {quantity}, Price: ${price}"
print(formatted_string_f_string)