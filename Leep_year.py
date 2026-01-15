#   Write a Python program to check if a year is a leap year.
year=int(input("Enter the Yaer-::"))
if(year%400==00 or year%4==0) and (year%100!=0):
    print("Leep yaer")
else:
    print("not leep yeer")