# . Write a Python program to merge two lists and remove duplicates.
a=[23,4,2,4,2,424,32]
b=[42,424,52,4,35234,32,523,2]
marge=[]

for i in a:
    found=False
    for j in marge:
        if (i==j):
            found=True
    if(found==False):
        marge=marge+[i]
for i in b:
    found=False
    for j in marge:
        if(i==j):
            found=True
    if(found==False):
        marge=marge+[i]
print("merge list here-::",marge) 