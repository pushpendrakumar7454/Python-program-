
# 24.Write a Python program to find the missing number in a list from 1 to N.
lst=[2,3,2,5,6,4,8,9]
l=10
n=[]

for i in range(1,l+1):
    if i not in lst:
        n.append(i)

print(n)   