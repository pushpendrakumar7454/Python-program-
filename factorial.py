# Write a Python program to find the factorial of a number using a loop.


num=int(input("Enter the Number-::"))

fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)  