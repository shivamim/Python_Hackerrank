#TASK
'''Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.'''

#SOLUTION 

    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))