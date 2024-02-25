#TASK 
'''Create a new list from two list using the following condition: Given two list of numbers,
write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.'''

#SOLUTION

list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))

list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

new_list = []


for num in list1:
    if num % 2 != 0:  # Check if the number is odd
        new_list.append(num)


for num in list2:
    if num % 2 == 0:  # Check if the number is even
        new_list.append(num)

print("The new list containing odd numbers from the first list and even numbers from the second list is:", new_list)
