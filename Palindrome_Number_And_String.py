
#.Write a Python program to check if a string is a palindrome.
# From number
import math
num=int(input("Enter the Number-::"))
rev=0
temp=num

while(temp>0):
    a=(temp % 10)
    rev=rev * 10 + a
    temp=temp//10

if(rev==num):
    print('is Palindrome')
else:
   print ('is not Palindrome')

# From String----

str=input("Enter the  String-::")
rev=''
for i in str:
    rev=i+rev
if(str==rev):
    print("Palindrome")
else:
    print("not palindrome")  

    # or
    String=input("Enter the String-::")
rev=''

for i in range(len(String)-1,-1,-1):
    rev=rev+String[i]
if(rev==String):
    print("palindrome")    
else:
    print("NOT palindrome")