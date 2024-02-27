#TASK 
'''You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.'''

#SOLUTION
if __name__ == '__main__':
    s = input()

res = False
for i in s:
    if i.isalnum():
        res = True
        break
print(res)

res = False
for j in s:
    if j.isalpha():
        res = True
        break
print(res)

res = False
for k in s:
    if k.isdigit():
        res = True
        break
print(res)

res = False
for l in s:
    if l.islower():
        res = True
        break
print(res)

res = False
for l in s:
    if l.isupper():
        res = True
        break
print(res)
            