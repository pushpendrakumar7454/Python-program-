# 22.Write a Python program to remove all duplicates from a string.
p="programming"
result=''

for i in p:
    if i not in result:
        result=result+i
print(result)    