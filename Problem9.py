#TASK 
'''Check Palindrome Number'''

num = int(input("Enter your number:"))
original_num= num 
reversed_num=0
while num > 0:
    last_digit = num%10
    reversed_num = (reversed_num * 10) + last_digit
    num = num // 10
if original_num == reversed_num:
    print('Number is palindrome')
else:
    print('Number is not palindrome')