# 9. Write a Python program to check whether a number is an Armstrong number.
import math
num=int(input("Enter the Number-::"))
temp=num
sum=0
count=len(str(num))
while(temp>0):
    a=math.floor(temp%10)
    sum=sum+a**count
    temp=temp//10

if(sum==num):
    print("ArmStrong")
else:
    print("Not Armstong")