# Write a Python program to replace all spaces in a string with underscores.

s=input("Enter the String-::")
re=""
for i in s:
    if i==" ":
        re+="_"
    else:
        re+=i
print(re) 