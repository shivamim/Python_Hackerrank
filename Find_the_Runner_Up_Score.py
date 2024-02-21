#TASK 
'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format:

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints:

2<=n <=10
-100 <=A[i] <= 100'''

#SOLUTION

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = list(set(arr))
    arr2.sort()
    print(arr2[-2]) 