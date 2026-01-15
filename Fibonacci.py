# Write a Python program to print all Fibonacci numbers less than 100.
a=0
b=1
print(a,end=" ")
while(b<100):
    print(b,end=" ")
    c=a+b
    a=b
    b=c
