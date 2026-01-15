#  Write a Python program to check if a list is symmetric (same forwards and backwards).
ls=[23,34,34,23,3] 
flag=True
for i in range (len(ls)):
    if ls[i]!=ls[-i-1]:
        flag=False
        break
if flag:
    print("symmetric")
else:
    print("not symmetric")     
