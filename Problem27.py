#TASK 
''' Write a program to print multiplication table of a given number'''

#SOLUTION 
num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")

i = 1

while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")
    i += 1  
