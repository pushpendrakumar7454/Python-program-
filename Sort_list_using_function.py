# .Write a Python program to sort a list without using the sort() function.

def sort():
    a=[34,22,32,34,3232,22,24,232,4,32,4,52,4325,2,4,235,2,42,52,2,324]  

    n=len(a)

    for i in range(n):
       for j in range (0,n-i-1):
         if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
    print(a)    
sort() 