#Juan Taylor 04/24/2023 Module 9 assignment
#Program uses classes to create a banking program.
import random
#complete tasks: will need to run the program twice. Once with the account balance of $200
#  and once with the acct bal of $25. Since the second run of the program will have a balance 
# lower than the minimum balance, a message should be output letting the user know that 
# their account is below the minimum balance. Incorporate the good coding practices you have
#  learned up to this point in the course such as Try/Except Blocks, allow the user to 
# continue to run the program, and to exit the program, formatting methods, etc.

#****************************BANK ACCOUNT CLASS***************************
class BankAccount:
    #attributes
    def __init__(self, accountNumber, balance):
        self.accountNumber = int(accountNumber)
        self.balance = balance
        print("Your account has been created.")

#functions
    def withdraw(self, fundsDeducted):
        try:    
            fundsDeducted = float(input("How much would you like to withdraw today: "))
            if self.balance > fundsDeducted and type(float):
                self.balance -= fundsDeducted 
                print("Amount withdrawn: " + "$" + str(fundsDeducted) + ". Current balance is now $" + str(self.balance))
            else:
                print("Insufficient Funds")
        except:
            print("Please enter a valid number")

    def deposit(self, fundsAdded):
        try:
            fundsAdded = float(input("How much would you like to deposit today: "))
            if fundsAdded > 0:
                self.balance += fundsAdded 
                print("Amount deposited: " + "$" + str(fundsAdded) + ". Current balance is now $" + str(self.balance))
            else:
                print("Deposit cannot be zero or negative")
        except:
            print("Please enter a valid number")

#Getters
    def getBalance(self):
        print("Current balance is $" + str(self.balance) + ".")

    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, acctNum):
        self.accountNumber = acctNum

    def setBalance(self, initialAmt):
        self.balance = initialAmt

#****************************CHECKING ACCOUNT CLASS***************************
class CheckingAccount(BankAccount):
    #attributes
    def __init__(self, accountNumber, balance, fees, minimumBalance):
        super().__init__(accountNumber, balance)
        self.fees = int(fees)
        self.minimumBalance = float(minimumBalance)

#functions
    def deductFees(self):
        self.balance -= self.fees
        print("Your balance is below the minimum requirement you have been charged a checking account fee of $" + str(self.fees) + ".")
        
    def checkMinimumBalance(self):
        if self.balance < self.minimumBalance:
            self.deductFees()
            print("Your current balance is: $" + str(self.balance) + ".")
        else:
            print("Your current balance is: $" + str(self.balance) + ".")

#function override
    def withdraw(self, fundsDeducted):
        try:
            fundsDeducted = float(input("How much would you like to withdraw today: "))
            if self.balance > fundsDeducted and type(float):
                self.balance -= fundsDeducted 
                print("Amount withdrawn: " + "$" + str(fundsDeducted) + ".")
                self.checkMinimumBalance()
            else:
                print("Insufficient Funds")
        except:
            print("Please enter a valid number")

#Getters
    def getBalance(self):
        print("Current balance is $" + str(self.balance) + ".")

    def getAccountNumber(self):
        return self.accountNumber
    
    def getFees(self):
        return self.fees
    
    def getMinimumBalance(self):
        return self.minimumBalance

#Setters    
    def setBalance(self, initialAmt):
        self.balance = initialAmt
    
    def setAccountNumber(self, acctNum):
        self.accountNumber = acctNum

    def setFees(self, fee):
        self.fees = fee

    def setMinimumBalance(self, reqBal):
        self.minimumBalance = reqBal

#****************************SAVINGS ACCOUNT CLASS***************************
class SavingsAccount(BankAccount):
    #attributes
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate
    
#working on savings account functioons
    def addInterest(self):
        compoundedInterest = (self.balance * self.interestRate) 
        self.balance = compoundedInterest + self.balance
        print("Your total interest added this year is $" + str(compoundedInterest) + "Current balanace including interest is $" + self.balance)

#Getters
    def getBalance(self):
        print("Current balance is $" + str(self.balance) + ".")
        print("Current interest rate: " + str(self.interestRate) + ".")

    def getAccountNumber(self):
        return self.accountNumber
    
    def getInterestRate(self):
        return self.interestRate

#Setters    
    def setBalance(self, initialAmt):
        self.balance = initialAmt
    
    def setAccountNumber(self, acctNum):
        self.accountNumber = acctNum

    def getInterestRate(self, rate):
        self.interestRate = rate
    
#program
def stellar_bank_program():
    acct = None
    print()
    print("Welcome To Stellar Bank!")
    print()

#open A account type
    def openAcct():
        openingAcct = True
        acctOption = 0
        accountNumber = random.randint(1000, 10000)
        balance = 0
        fees = 0
        minimumBalance = 0
        while openingAcct:
            print("")
            try:
                acctOption = int(input("Open a Checking press 1 or Savings press 2!\n"))
                if acctOption == 1:
                    print("Checking account Opened")
                    accountNumber = random.randint(1000, 10000)
                    balance = 0
                    fees = 0
                    minimumBalance = 0
                    openAcctState = 0
                    creatingChecking = True

                    while creatingChecking:
                        match openAcctState:
                            case 0:
                                balance = float(input("Please enter you opening balance: "))
                                try:
                                    if balance > 0:
                                        print("Your opening balance is $" + str(balance))
                                        openAcctState = 1
                                    else:
                                        print("Error -- Balance cannot be zero or negative")
                                except:
                                    print("\nError -- Please enter a valid number\n")
                            case 1:
                                minimumBalance = 50
                                fees = 5
                                print("Your fees are $5 whenever your Checking account balance reaches below $50.")
                                print("")
                                openAcctState = 2
                            case 2:
                                return CheckingAccount(accountNumber, balance, fees, minimumBalance)
                if acctOption == 2:
                    print("Saving account Opened")
                    accountNumber = random.randint(1000, 10000)
                    balance = 0
                    interestRate = 0
                    openAcctState = 0
                    creatingSaving = True

                    while creatingSaving:
                        match openAcctState:
                            case 0:
                                balance = float(input("Please enter you opening balance: "))
                                try:
                                    if balance > 0:
                                        print("Your opening balance is $" + str(balance))
                                        openAcctState = 1
                                    else:
                                        print("Error -- Balance cannot be zero or negative")
                                except:
                                    print("\nError -- Please enter a valid number\n")
                            case 1:
                                if balance > 0:
                                    interestRate = .02
                                    print("Your Savings account interest rate is 2%.")
                                    openAcctState = 2
                            case 2:
                                return SavingsAccount(accountNumber, balance, interestRate)

                    break
            except:
                print("\nError -- Please enter a valid number\n")

    menuOption = 0

    menuActive = True
    acct = None

    while menuOption != 5:
        #display menu option
        bank_menu = {1: "Open Account", 2: "Check Balance", 3: "Deposit Money", 4: "Withdraw Money", 5: "Quit"}

        options = bank_menu.keys()
        for entry in options: 
            print(entry, bank_menu[entry])

        menuActive = True

        while menuActive:
            try:
                menuOption = int(input("Please enter an option: "))
                if 0 < menuOption < 6:
                    menuActive = False    
                else:
                    print("\nPlease enter a number greater than 0 and less than 6\n")
                    options = bank_menu.keys()
                    for entry in options: 
                        print(entry, bank_menu[entry])
            except:
                print("\nPlease enter a number between 1 to 5 only\n")
                options = bank_menu.keys()
                for entry in options: 
                    print(entry, bank_menu[entry])
        
        if menuOption == 1:
            acct = openAcct()
        elif menuOption == 2:
            print("")
            acct.getBalance()
            print("")
        elif menuOption == 3:
            print("")
            fundsAdded = 0
            acct.deposit(fundsAdded)
            print("")
        elif menuOption == 4:
            print("")
            fundsDeducted = None
            acct.withdraw(fundsDeducted)
            print("")
        elif menuOption == 5:
            print("quit")
            menuActive = False

stellar_bank_program()