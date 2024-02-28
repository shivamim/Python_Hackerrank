#TASK 
'''Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.'''

#SOLUTION 
def square(base,expo):
   return base**expo



base_input=int(input("what is base:"))
expo_input=int(input('enter expo:'))
result= square(base_input,expo_input)
print(f'{base_input} raised to the power {expo_input} is:{result}')