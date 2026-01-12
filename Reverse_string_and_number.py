# 4. Write a Python program to reverse a string without using built-in functions.  
# from number
import math
def reverse():
    num=int(input("Enter the Number-::"))
    rev=0
    temp=num
    while temp>0:
        a=math.floor(temp%10)
        rev=rev*10+a
        temp=temp//10
    print(rev)

reverse()   


# from String
def Reverse():
   String=input("Enter the Number-::") 
   s='' 
   for i in String:
      s=i+s
   print(s)  
Reverse()         