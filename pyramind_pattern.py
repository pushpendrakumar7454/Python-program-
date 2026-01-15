
#  Write a Python program to print a pyramid pattern of numbers.

num=int(input("Enter the numbers-::"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()