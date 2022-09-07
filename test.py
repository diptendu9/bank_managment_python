import sys
from unicodedata import name

try:
    open("data.txt")
except:
    open("data.txt", "x")

class bank:
    users=[]
    # def __init__(self,*argv):
    #     # self.users=[]
        
    #     acc= argv[0]
    #     id=argv[1]
    #     balance=argv[2]  
    def login(self):
        i=0
        while(i==0):
            try:
                acc=int(input('Enter Account No :'))
            except:
                print("Enter a valid integer: ")
            # passid=input('Enter Password :')
            if acc not in self.users:
                print('Invalid Account No: ')
            if acc in self.users:
                i=i+1
            # else:
            #      print('Not Registered')
        def show():
            print('abc')
    
    def register(self):
        # while(True):
        try:
            acc=int(input('Enter Account No :'))
        except:
            print("Enter a valid integer: ")
        
        username=input('Enter User Name: ')
        bal=int(input("Enter Balance: "))
        # passid=input('Enter Password :')
        # passid1=input('Confirm Password :')
        # if(passid != passid1):
        #     print('Password not matched')

        f= open("data.txt", "a")
        # f.write(str(username)+str(acc)+" "+str(bal))
        f.write("name : "+str(username)+" , "+"Account No : "+str(acc)+" , "+"Balance : "+str(bal)+"\n")
        fi = open(username+".txt", "x")
        fi.write("name : "+str(username)+" , "+"Account No : "+str(acc)+" , "+"Balance : "+str(bal)+"\n")
            #self.users[-1].append(acc,userid,passid)


a = bank()

# while()

a.register()
#a.login()


