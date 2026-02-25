import random
import json
import string
from datetime import datetime

class Bank:
    admin_id = "admin"
    admin_password = "1234"

    def __init__(self):
        self.current_user = None
        self.admin_logged = False

    database = "bank.json"
    bank = []

    try:
        with open(database) as fs:
            bank = json.load(fs)
    except Exception as err:
        print(err)

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.bank, indent=4))

    @classmethod
    def __createaccount(cls):
        stringse = random.choices(string.ascii_letters, k=5)
        digit = random.choices(string.digits, k=4)
        spe = random.choices("!@#$%^&*", k=5)
        id = stringse + digit + spe
        return "".join(id)

    def accountcreate(self):
        info = {
            'name': input("Enter yourr name-::"),
            "pin": int(input("Enter your pin-::")),
            'accountno': Bank.__createaccount(),
            'balance': 0,
            'age': int(input("Enter your age-::")),
            'transactions': []
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Do not create account")
            return

        print("Accountt created succefully")
        Bank.bank.append(info)
        Bank.__update()

    def depositamount(self):
        acountno = input("Enter yourr account no-::")
        pin = int(input("Enter your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == acountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User not found")
        else:
            if not self.current_user:
                print("Please login first ")
                return

            amount = int(input("Ener your amount you deposit-::"))
            if amount > 10000 or amount < 0:
                print("No not deposit amount")
            else:
                userdata[0]['balance'] += amount
                print("Amount deposit succefully")
                self.current_user['transactions'].append({
                    "type": "deposit",
                    "amount": amount,
                    "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                })
                Bank.__update()

    def withdrowamount(self):
        accountno = input("enter your accunt no.::")
        pin = int(input("Entr your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == accountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User not found")
        else:
            if not self.current_user:
                print("Please login first ")
                return

            amount = int(input("Enter your amount you withdrow-::"))
            if amount > 10000 or amount < 0:
                print("Do not deposit")
            else:
                userdata[0]['balance'] -= amount
                self.current_user['transactions'].append({
                    "type": "withdraw",
                    "amount": amount,
                    "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                })
                print("amount withdrow succefully")
                Bank.__update()

    def viewuser(self):
        accountno = input("Enter your account no-::")
        pin = int(input("Enter your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == accountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User nott found")
        else:
            if not self.current_user:
                print("Please login first ")
                return

            print("----- User Details -----")
            for key, value in userdata[0].items():
                print(f"{key} : {value}")

    def updateuser(self):
        accountno = input("Enter your account no-::")
        pin = int(input("Enter your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == accountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User not found")
        else:
            name = input("Enter your new name-::")
            pin = int(input("Enter your new pin-::"))

            userdata[0]['name'] = name
            userdata[0]['pin'] = pin

            print("User update profile succefully")
            Bank.__update()

    def deleteuser(self):
        accountno = input("Enter your acccountno-::")
        pin = int(input("Enter your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == accountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("User not found")
        else:
            check = input("Enter your choice y used too delete your account and n used too bypassed your-::")
            if check == 'n':
                print("Bypassed")
            else:
                index = Bank.bank.index(userdata[0])
                Bank.bank.pop(index)

                print("User profile deletted succefuuly")
                Bank.__update()

    def checkbalance(self):
        acountno = input("Enter your account no-::")
        pin = int(input("Enter your pin-::"))
        userdata = []

        for i in Bank.bank:
            if i['accountno'] == acountno and i['pin'] == pin:
                userdata.append(i)

        if not userdata:
            print("user not found")
        else:
            check = input("check your balance to press yes and exit or account use to exit button-::")
            if check == "e" or check == "Exit":
                print("Exit your account succefully")
            else:
                print(f"{userdata[0]['name']} Your balance is now {userdata[0]['balance']}")

    def moneytranceferfeature(self):
        sender_acc = input("Enter your Sender account no.-::")
        pin = int(input("Enter your pin-::"))
        reciever_acc = input("Enter your reciever account no-::")
        amount = int(input("Enter your amount you send-::"))

        sender = None
        reciever = None

        for i in Bank.bank:
            if i['accountno'] == sender_acc and i['pin'] == pin:
                sender = i
            if i['accountno'] == reciever_acc:
                reciever = i

        if not sender:
            print("Sender account is not found and pin is so wrong")
            return

        if not reciever:
            print("Reviever  account is not found")
            return

        if amount < 0:
            print("amount is too low")
            return

        if sender['balance'] < amount:
            print("Insufficient balance")
            return

        sender['balance'] -= amount
        reciever['balance'] += amount

        sender['transactions'].append({
            "type": "transfer_sent",
            "amount": amount,
            "to": reciever_acc,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        reciever['transactions'].append({
            "type": "transfer_received",
            "amount": amount,
            "from": sender_acc,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        print("Amount transferred successfully")
        Bank.__update()

    def login(self):
        if self.current_user:
            print("User already logged in")
            return

        accountno = input("Enter account no-::")
        pin = int(input("Enter pin-::"))

        for user in Bank.bank:
            if user['accountno'] == accountno and user['pin'] == pin:
                self.current_user = user
                print("Login successful ")
                return

        print("Invalid account number or PIN")

    def logout(self):
        if self.current_user:
            print("Logout successful ")
            self.current_user = None
        else:
            print("No user is logged in")

    def viewtransactions(self):
        if not self.current_user:
            print("Please login first")
            return

        if not self.current_user['transactions']:
            print("No transactions found")
            return

        print("----- Transaction History -----")
        for t in self.current_user['transactions']:
            print(t)

    def adminlogin(self):
        if self.admin_logged:
            print("Admin already logged in")
            return

        admin_id = input("Enter admin id-::")
        password = input("Enter admin password-::")

        if admin_id == Bank.admin_id and password == Bank.admin_password:
            self.admin_logged = True
            print("Admin login successful ")
        else:
            print("Invalid admin credentials ")

    def adminlogout(self):
        if self.admin_logged:
            self.admin_logged = False
            print("Admin logout successful ")
        else:
            print("Admin not logged in")

    def viewallusers(self):
        if not self.admin_logged:
            print("Admin login required ")
            return

        if not Bank.bank:
            print("No users found")
            return

        print("----- All Bank Users -----")
        for user in Bank.bank:
            print(f"Name: {user['name']}")
            print(f"Account No: {user['accountno']}")
            print(f"Balance: {user['balance']}")
            print("-------------------------")

    def totalbankbalance(self):
        if not self.admin_logged:
            print("Admin login required ")
            return

        total = 0
        for user in Bank.bank:
            total += user['balance']
        print(f"Total Bank Balance: {total}")

    def totalaccounts(self):
        if not self.admin_logged:
            print("Admin login required ")
            return

        print(f"Total Accounts: {len(Bank.bank)}")


banks = Bank()

while True:

    if banks.admin_logged:
        print("""
        ----- ADMIN PANEL -----
        1. View All Users
        2. Total Bank Balance
        3. Total Accounts
        4. Admin Logout
        """)

        choice = int(input("Enter choice-::"))

        if choice == 1:
            banks.viewallusers()
        elif choice == 2:
            banks.totalbankbalance()
        elif choice == 3:
            banks.totalaccounts()
        elif choice == 4:
            banks.adminlogout()
        else:
            print("Invalid choice")

    elif banks.current_user:
        print(f"""
        --- Welcome {banks.current_user['name']} ---
        1. Deposit amount
        2. Withdraw amount
        3. View user
        4. Update user
        5. Delete user
        6. Check balance
        7. Money transfer
        8. View transactions
        9. Logout
        """)

        check = int(input("Enter your choice-::"))

        if check == 1:
            banks.depositamount()
        elif check == 2:
            banks.withdrowamount()
        elif check == 3:
            banks.viewuser()
        elif check == 4:
            banks.updateuser()
        elif check == 5:
            banks.deleteuser()
        elif check == 6:
            banks.checkbalance()
        elif check == 7:
            banks.moneytranceferfeature()
        elif check == 8:
            banks.viewtransactions()
        elif check == 9:
            banks.logout()
        else:
            print("Invalid choice")

    else:
        print("""
        ----- MAIN MENU -----
        1. Create Account
        2. User Login
        3. Admin Login
        4. Exit
        """)

        choice = int(input("Enter choice-::"))

        if choice == 1:
            banks.accountcreate()
        elif choice == 2:
            banks.login()
        elif choice == 3:
            banks.adminlogin()
        elif choice == 4:
            print("Thank You | Exit")
            break
        else:
            print("Invalid choice")