#TASK 
'''Print a downward Half-Pyramid Pattern of Star (asterisk)'''

#SOLUTION
rows = int(input("Enter the number of rows for the downward half-pyramid: "))

# Print the downward half-pyramid pattern
print("\nDownward Half-Pyramid Pattern:\n")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()