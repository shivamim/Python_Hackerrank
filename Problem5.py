#TASK 
'''Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.'''

#SOLUTION 
def listchecker(lst):
    if len(lst) > 0:
        if lst[0] == lst[-1]:
            return True
        else:
            return False
    else:
        print("List is empty!")

user_input = input("Enter a list of numbers separated by spaces: ")

# Remove commas from the input string and split into a list
user_list = [int(num.replace(',', '')) for num in user_input.split()]

result = listchecker(user_list)

if result:
    print("The first and last numbers of the list are the same.")
else:
    print("The first and last numbers of the list are not the same.")

