def Add(A,B):
    print("Add is=",A+B)

def Subtraction(A,B):
    print("Sub is=",A-B)

def Multipliction(A,B):
    print("Multipliction is=",A*B)

def Divide(A,B):
    print("Divide is=",A/B)

print("calling functions")
Add(4,9)
Subtraction(44,3)
Multipliction(4,7)
Divide(30,10)

#Default Parameter Value
def IpUserName(UserName="DefaultUser1"):
   print("User is->" + UserName)

IpUserName("John")
IpUserName("Nick")
IpUserName()
IpUserName("jj")