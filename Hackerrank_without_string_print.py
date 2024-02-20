'''The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n   Note that "..." represents the consecutive values in between.'''

#SOLUTION

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')          
        
'''it then takes input from the user in the form of an integer, assigns it to the variable "n", and then uses a for loop to iterate over a range of numbers from 1 to n+1.
Within the loop, it then prints the current iteration number, with the "end" parameter set to an empty string, which means that each number will be printed on the same line, rather than on a new line.'''