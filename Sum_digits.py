#  Write a Python program to find the sum of digits of a number.

a=3,43,65,765
sum=0
for i in a:
    sum=sum+i
print(sum)  
# -----------list se------------ 
a=[2,8,40]
sum=0
total=[]

for i in a:
    sum=sum+i
    total.append(sum)
print(total[-1:]) 