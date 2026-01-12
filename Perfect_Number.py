 # Write a Python program to check if a number is a perfect number. 
Perfect_number=int(input("Enter the Number-::"))

num=0

for i in range(1,Perfect_number):
    if(Perfect_number%i==0):
        num=num+i
if(Perfect_number==num):
    print(f"{Perfect_number} Is Perfect Number") 
else:
    print(f"{Perfect_number} is Not Perfect Number")    
