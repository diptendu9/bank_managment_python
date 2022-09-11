from curses.ascii import isdigit
from math import nan
from random import randint, randrange
from unicodedata import name
import pathlib
import os, pickle


class Person:
    #name=''
    def __init__(self):
        self.aadhaar =''
        self.name= ''
        self.accn = 0
    def customer(self):
        while(True):
            Person.name=input("Enter your Aadhaar No: ")
            if(Person.name.isdigit()):
                break
        
        while(True):
            Person.accn= input("Enter account No:  ")
            if(Person.accn.isdigit() and int(Person.accn)>0):
                break
        
        #self.name = input("Enter your name: ")
        while(True):
            Person.name=input("Enter your name: ")
            if(Person.name.isalpha()):
                break
    # def showname(self):
    #     print(self.name)

class Bank(Person):
    
    cno = 'NA'
    dno= 'NA'
    cheque =0
    def __init__(self):  #Initial Variables Constructor 
        Person.__init__(self)
        # self.accn= 000
        # self.name=''
        self.acctype=''
        self.balance= 0
        self.cno = 'NA'
        self.dno= 'NA'
        self.cheque =0
        #super.name = ''

    
    def createAccn(self): 
        '''Function to Create an Account'''
        # while(True):
        #     self.accn= input("Enter account No:  ")
        #     if(self.accn.isdigit() and int(self.accn)>0):
        #         break
        
        # #self.name = input("Enter your name: ")
        # while(True):
        #     self.name=input("Enter your name: ")
        #     if(self.name.isalpha()):
        #         break

        while(True):
            self.acctype = input("Enter S for Savings, C for Current: ")
            if(self.acctype == 'S' or self.acctype =='C'):
                break
        while(True):
            self.balance=input("Initial balance if Current account then min balance should be 1000, If savings then min balance should be 2000: ")
            if(self.acctype=='S' and int(self.balance)>=2000): break
            if(self.acctype=='C' and int(self.balance)>=1000):break

        print("\t \tWelcome to Bank \n")

    def showbalance(self, i):
        '''Function to Show Balance'''
        #print(self.name)
        print("Account Number:" + str(i.accn))
        print("Account Holder Name:" + str(i.name))
        print("Balance: " + str(i.balance)+'\n')

    def downstate(self, i):
        '''Function to Download and print Bank Statement with name as filename'''
        fi = open(i.name+".txt", "w")
        fi.write('\t----Bank Satatement----\t \n'+"Account Number : "+ str(i.accn)+"\nCustomer Name: "+str(i.name)+"\nAccount Type: "+str(i.acctype)+ "\nCurrent Balance: "+str(i.balance)+'\n')
        fi.write("Credit Card: "+str(i.cno)+'\n')
        fi.write("Debit Card: "+str(i.dno)+'\n')
        fi.write("Issued Cheque: "+str(i.cheque)+'\n')
        print("Sucessfully Generated ! \n")

        print('\t----Bank Satatement----\t \n'+"Account Number : "+ str(i.accn)+"\nCustomer Name: "+str(i.name)+"\nAccount Type: "+str(i.acctype)+ "\nCurrent Balance: "+str(i.balance)+'\n')
        print("Credit Card: "+str(i.cno)+'\n')
        print("Debit Card: "+str(i.dno)+'\n')
        print("Issued Cheque: "+str(i.cheque)+'\n')

        

    def deposit(self,i, a):
        '''Function to Deposit balance in account'''

        # try:
        #     amt = int(input("Enter amount to Deposit: "))
        #     self.balance = int(self.balance)+ abs(amt)
        # except:
        #     print("Invalid input. Enter only integers !")
        i.balance = int(i.balance) + int(a)
        print("Transaction Successfull \n")

    def withdraw(self,i, amt):
        '''Function to Withdraw balance form account'''

        # try:
        #     amt = int(input("Enter amount to Withdraw: "))
        #     i.balance = int(self.balance) - abs(amt)
        # except:
        #     print("Invalid input. Enter only integers !")
        i.balance = int(i.balance) - int(amt)
        print("Transaction Successfull \n")

    def newcredit(self, i):
        '''Function to Issue a Credit Card with 12 to 14 digit number'''

        i.cno= str(randrange(100000000000, 100000000000000))
        print("\t Success \n")
    
    def newdebit(self,i):
        '''Function to issue a debit card of 12 to 14 digits'''

        i.dno= str(randrange(100000000000, 100000000000000))
        print("\t Success \n")
    
    def newcheque(self, i):
        '''Function to issue Cheque Book and rthe cost is deducted'''

        print("Please Note Cheque book price is 100, which will be deducted from account")
        i.cheque += 1
        i.balance =int(i.balance)-100
        print("\t Successfully Issued\n")










    
def writeAccount():
    account = Bank()
    account.customer()
    account.createAccn()
    writeAccountsFile(account)

# Function to display all the details

def displayAll():
    account=Bank()
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")

def statement(num):
    #account=Bank()
    account=Bank()
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        #os.remove('accounts.data')
        for item in mylist :
            if item.accn == str(num):
                account.downstate(item)
    else:
        print("Not Found")

# Function to display the account balance if a record is present
def displaybal(num):
    account = Bank()
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            #print(item.accn)
            if item.accn == str(num) :

                account.showbalance(item)
                # Bank.showbalance( item)
                # print("Your account Balance is = ",item.balance)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")


# Function to allow the deposit and withdraw transaction to occur
def depositAndWithdraw(num1,num2):
    account=Bank()
    file = pathlib.Path("accounts.data")
    infile = open('accounts.data','rb')
    mylist = pickle.load(infile)

    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        # os.remove('accounts.data')
        for item in mylist :
            if item.accn == str(num1) :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    account.deposit(item, amount)
                    print("Transaction Sucessfull money credited")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.balance:
                        account.withdraw(item, amount)
                        # item.deposit -=amount
                        print("Transaction Sucessfull money debited")

                    else :
                        print("You cannot withdraw larger amount")

    else :
        print("No records to Search")
    outfile = open('accounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    # os.rename('newaccounts.data', 'accounts.data')

# def deleteAccount(num):
#     file = pathlib.Path("accounts.data")
#     if file.exists ():
#         infile = open('accounts.data','rb')
#         oldlist = pickle.load(infile)
#         infile.close()
#         newlist = []
#         for item in oldlist :
#             if item.accn != num :
#                 newlist.append(item)
#         os.remove('accounts.data')
#         outfile = open('newaccounts.data','wb')
#         pickle.dump(newlist, outfile)
#         outfile.close()
#         os.rename('newaccounts.data', 'accounts.data')



# function to write into accounts file
def writeAccountsFile(account) :
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

def modifyproduct(num,action):
    """
    Reads data from accounts.data
    Finds matched account number from num1
    calls modifyCards() passing the account matched as 'item' and choice as num2
    """
    account = Bank()
    file = pathlib.Path("accounts.data")
    infile = open('accounts.data','rb')
    mylist = pickle.load(infile)
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        # os.remove('accounts.data')
        for item in mylist :
            if item.accn == str(num):
                if(action == 1):
                    account.newdebit(item)
                elif(action==2):
                    account.newcredit(item)
                elif(action==3):
                    account.newcheque(item)
    else :
        print("No records found")
    outfile = open('accounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    # os.rename('newaccounts.data', 'accounts.data')


n =''
# c= Person()
# p= Bank()  #Create object from class

print("\n --------BANK SYSTEM------------- \n")
while(n!=10):  #Loop to take choices
    print("1. Create Customer")
    print("2. Create Account ")
    print("3. Show Balance ")
    print("4. Download Statement")
    print("5. Deposit Amount")
    print("6. Withdraw Amount ")
    print("7. Add Debit Card")
    print("8. Add Credit Card")
    print("9. Add Cheque Book")
    print("10. Exit ")
    n=input("Enter a Choice: ")
    
    if n=='10':     #Conditions to perform according to the entered choice 
        print("******** Thank You ******* \n")
        break
    elif n=='1':
        Person.customer(Person)
    elif n=='2':
        writeAccount()
    elif n=='3':
        num= int(input("Enter account No: "))
        displaybal(num)
    elif n=='4':
        ac= int(input("Enter account nymber:"))
        statement(ac)
        #p.downstate()
    elif n=='5':
        num= int(input("Enter account No: "))
        depositAndWithdraw(num,1)
    elif n=='6':
        num= int(input("Enter account No: "))
        depositAndWithdraw(num,2)
    elif n=='7':
        num= int(input("Enter account No: "))
        modifyproduct(num, 1)
    elif n=='8':
        num= int(input("Enter account No: "))
        modifyproduct(num, 2)
    elif n=='9':
        num= int(input("Enter account No: "))
        modifyproduct(num, 3)
