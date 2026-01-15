# Write a Python program to find the second largest number in a list.

num=[12,34,54,198,200,34,54]
Largest=0
smalest=0

for i in num:
    if (i>Largest):
        smalest=Largest
        Largest=i
    elif(i>smalest) and(i!=Largest):
        smalest=i
print(smalest)   