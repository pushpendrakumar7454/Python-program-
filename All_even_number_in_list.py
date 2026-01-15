#  Write a Python program to find all even numbers in a list.

lists=[2,32,3,44,3,2423,4,2352,52,3]
even_list=[]

for i in lists:
    if(i%2==0):
        even_list=even_list+[i]
print(even_list)