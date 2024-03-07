#TASK 
'''Calculate the sum of all numbers from 1 to a given number'''

#SOLUTION

num=int(input('Enter your number upto which you want to add up:'))
sum=0
for i in range(1,num+1):
    sum +=i
    
print(f'The sum of input value is: {sum}')
    