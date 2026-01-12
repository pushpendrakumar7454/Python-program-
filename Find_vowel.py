
# Write a Python program to count the number of vowels in a string.

text=input("Enter the String-::")
vowel='AEIOUaeiou'
count=0
for i in  text:
    if i in vowel:
        count=count+1
print(count)  