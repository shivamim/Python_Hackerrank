#TASK 
'''Display numbers from a list using loop'''

#SOLUTION 

user = input("Enter a list of numbers separated by spaces: ")
user_list_str = user.split()
user_list = [int(num) for num in user_list_str]
for i in range(len(user_list)):
    print(user_list[i])

