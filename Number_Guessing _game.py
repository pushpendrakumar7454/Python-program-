import random
count=0
userinput=0
computerinput=0
max_count=10

while(count<max_count):
    computer=random.randint(1,3)
    user=int(input("Enter the number-::"))

    count=count+1

    if(user==0):
        print("Thank You!!")
        print("exit")
        exit()
    elif(user==computer):
        print(f"User Guess is {user} and Computer Guess is {computer} So User {userinput+1} Time is correct Guess")
        userinput=userinput+1
    else:
        print(f"User Guess is {user} and Computer Guess is {computer} So Computer {computerinput+1} Time is currect Guess")
        computerinput=computerinput+1

print("\n--Final Result--")
print()
if(computerinput>userinput):
    print(computerinput,"times is Computer Gusses correct  So Computer win!!")
elif(userinput>computerinput):
    print(userinput,"times is You Gusses correct  So You win!!")
elif(userinput==computerinput):
    print("draw")
else:
    print("thanku you!")
    exit()

print()    
    