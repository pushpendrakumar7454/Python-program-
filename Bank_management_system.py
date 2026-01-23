import string
import json
import random
from  pathlib import Path

class Bank:
    database='user.json'
    user=[]

    try:
        with open(database) as fs:
            user=json.loads(fs.read())
    except Exception as Err:
        print(Err)

    @classmethod
    def __update(cls):
        with open (cls.database,'w') as fs:
            fs.write(json.dumps(Bank.user))


    @classmethod
    def __accountcreate(cls):
        s=random.choices(string.ascii_letters,k=3)
        digit=random.choices(string.digits,k=3)
        speciel=random.choices("!@#$",k=3)
        id=(s+digit+speciel)
        random.shuffle(id)
        return "".join(id)

    def createacount(self):
        info={
            'name':input("Enter the name-::"),
            'email':input("Enter the email-::"),
            'age':int(input("ente the Age-::")),
            'pin':int(input("Enter the pin-::")),
            "accountno":Bank.__accountcreate(),
            'balance':0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("not created Account")
        else:
            print("Acount created Succefully")

        for i in info:
            print(f"{i} : {info[i]}")
            print("Note down your Acount No.")
        Bank.user.append(info)
        Bank.__update()

    def depositmoney(self):
        accountno=input("Enter the account no.-::")
        pin=int(input("Enter the pin-::"))

        userdata=[] 

        for i in Bank.user:
            if i['accountno']==accountno and i['pin']==pin:
                userdata.append(i)
        if not userdata:
            print("user not found")
        else:
            amount=int(input("Enter the amount You Deposit-::"))
            if amount>10000 and amount<0:
                print("amount to much so not deposit!")
            else:
                userdata[0]['balance']+=amount
                print("Your amount Depoist Succefully!")
                Bank.__update()           
    
    def withdrowmoney(self):
        acountno=input("Enter the account no.-::")
        pin=int(input("Enter tthe pin-::"))
        userdata=[]

        for i in Bank.user:
            if i ['accountno']==acountno and i['pin']==pin:
                userdata.append(i)

        if not userdata:
            print("user not found!")
        else:
            amount=int(input("Enter thee Withdrow amount-::"))      
            if amount>10000 or amount<0:
                print("Your Amount is To much so not Withdrow") 
            else:
                userdata[0]['balance']-=amount
                print("Your amount is withdrow Succefully!")
                Bank.__update()
    

    def showdetail(self):
       acountno=input("Enter thee account no.-::")
       pin=int(input("Enter the pin-::"))

       userdata=[]

       for i in Bank.user:
           if i['accountno']==acountno and i['pin']==pin:
               userdata=i
       if userdata:  
           for i in userdata:
               print(f"{i} : {userdata[i]}")
       else:
           print("user not found!")  

    def updatedetail(self):
        accountno = input("Enter the account no.-:: ")
        pin = int(input("Enter the Pin-:: "))

        userdata = []

        for i in Bank.user:
           if i['accountno'] == accountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User not found!")
            return

        print("You cannot change age, account number, balance!")
        print("Leave empty if no change\n")

        name = input("Enter the new Name-:: ")
        email = input("Enter the new Email-:: ")
        new_pin = input("Enter the new Pin-:: ")

        if name == "":
          name = userdata[0]['name']
        if email == "":
           email = userdata[0]['email']
        if new_pin == "":
           new_pin = userdata[0]['pin']
        else:
           new_pin = int(new_pin)

        userdata[0]['name'] = name
        userdata[0]['email'] = email
        userdata[0]['pin'] = new_pin

        Bank.__update()
        print("Detail updated Successfully!")

    def delete(self):
        accountno=input("Enter your Account no.-::")
        pin=int(input("Enter your pin-::"))

        userdata=[]

        for i in Bank.user:
            if i['accountno']==accountno and i['pin']==pin:
                userdata.append(i)

        if not userdata:
            print("user not found!")
        else:
            check=input("press Y if you actually want to delete the account or press n-:: ")
            if check=="n" or check=="N":
                print("bypassed")
            else:
                index=Bank.user.index(userdata[0])
                Bank.user.pop(index)
                print("account deleted Successfully!")
                Bank.__update()
        

users=Bank()
while True:
    print("""
1.Create Acount
2.Deposit Money
3.Withdrow Money
4.User Detail
5.Update Your Detail
6.Delete Accountt     
7.Exit             
""")

    choice=int(input("Enter your choice-::"))

    if choice==1:
       users.createacount()
    elif choice==2:
       users.depositmoney()
    elif choice==3:
        users.withdrowmoney()
    elif choice==4:
        users.showdetail()  
    elif choice==5:
       users.updatedetail()   
    elif choice==6:
        users.delete() 
    else:
        print("Thanku!Exit")
        break                     



