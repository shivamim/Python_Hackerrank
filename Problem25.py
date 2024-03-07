#TASK 
'''Write a program to print the following number pattern using a loop'''

#SOLUTION 
row = 1

while row <= 5:
    col = 1 
    
    while col <= row:  
        print(col, end=" ")  
        col += 1  
    
    print()  
    row += 1  
