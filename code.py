from math import nan
from random import randint, randrange
from unicodedata import name

class Person:
    
    def __init__(self):
        self.name =''
    def customer(self):
        while(True):
            self.name=input("Enter your name: ")
            if(self.name.isalpha()):
                break
    def showname(self):
        print(self.name)


class Bank(Person):
    def __init__(self):  #Initial Variables Constructor 
        # Person.__init__(self)
        self.accn=000
        #self.name=''
        self.acctype=''
        self.balance= 0
        self.cno = 'NA'
        self.dno= 'NA'
        self.cheque =0
        super.name = ''

    
    def createAccn(self): 
        '''Function to Create an Account'''
        try:
            self.accn=int(input("Enter account No: "))
        except:
            self.accn=int(input("Please Enter valid account No: "))
        #self.name = input("Enter your name: ")

        while(True):
            self.acctype = input("Enter S for Savings, C for Current: ")
            if(self.acctype == 'S' or self.acctype =='C'):
                break
        while(True):
            self.balance=input("Initial balance if Current account then min balance should be 1000, If savings then min balance should be 2000: ")
            if(self.acctype=='S' and int(self.balance)>=2000): break
            if(self.acctype=='C' and int(self.balance)>=1000):break

        print("\t \tWelcome to Bank \n")

    def showbalance(self):
        '''Function to Show Balance'''

        print("Account Number:" + str(self.accn))
        print("Account Holder Name:" + str(self.name()))
        print("Balance: " + str(self.balance)+'\n')

    def downstate(self):
        '''Function to Download a Statement with name as filename'''

        fi = open(self.name+".txt", "w")
        fi.write('\t----Bank Satatement----\t \n'+"Account Number : "+ str(self.accn)+"\nCustomer Name: "+str(self.name)+"\nAccount Type: "+str(self.acctype)+ "\nCurrent Balance: "+str(self.balance)+'\n')
        fi.write("Credit Card: "+str(self.cno)+'\n')
        fi.write("Debit Card: "+str(self.dno)+'\n')
        fi.write("Issued Cheque: "+str(self.cheque)+'\n')
        print("Sucessfully Generated ! \n")

    def deposit(self):
        '''Function to Deposit balance in account'''

        try:
            amt = int(input("Enter amount to Deposit: "))
            self.balance = int(self.balance)+ abs(amt)
        except:
            print("Invalid input. Enter only integers !")
        print("Transaction Successfull \n")

    def withdraw(self):
        '''Function to Withdraw balance form account'''

        try:
            amt = int(input("Enter amount to Withdraw: "))
            self.balance = int(self.balance) - abs(amt)
        except:
            print("Invalid input. Enter only integers !")
        print("Transaction Successfull \n")

    def newcredit(self):
        '''Function to Issue a Credit Card with 12 to 14 digit number'''

        self.cno= str(randrange(100000000000, 100000000000000))
        print("\t Success \n")
    
    def newdebit(self):
        '''Function to issue a debit card of 12 to 14 digits'''

        self.dno= str(randrange(100000000000, 100000000000000))
        print("\t Success \n")
    
    def newcheque(self):
        '''Function to issue Cheque Book and rthe cost is deducted'''

        print("Please Note Cheque book price is 100, which will be deducted from account")
        self.cheque += 1
        self.balance =int(self.balance)-100
        print("\t Successfully Issued\n")


n =''
p= Bank()  #Create object from class
c= Person()
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
        c.customer()
    elif n=='2':
        p.createAccn()
    elif n=='3':
        p.showbalance()
    elif n=='4':
        p.downstate()
    elif n=='5':
        p.deposit()
    elif n=='6':
        p.withdraw()
    elif n=='7':
        p.newdebit()
    elif n=='8':
        p.newcredit()
    elif n=='9':
        p.newcheque()
