#  Write a Python program to find the LCM (Least Common Multiple) of two numbers.
a=int(input("Enter the Number-::"))
b=int(input("Enter the Number-::"))

Lcm=max(a,b)

while True:
    if(Lcm%a==0) and (Lcm%b==0):
        print(Lcm)
        break
    Lcm=Lcm+1