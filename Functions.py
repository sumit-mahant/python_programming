def Gmean(a,b):
    mean=(a*b/(a+b))
    print(mean)

def isgreater(a,b):
    if(a>b):
     print("first number is greater.")

    else:
     print("second number is greater.")

def islesser(a,b):
   if(a<b):
      print("first number is smaller.")

   else:
      print("second number is smaller.")     
a=10
b=12
isgreater(a,b)
Gmean(a,b)
islesser(a,b)
if(a>b):
    print("first number is greater.")

else:
    print("second number is greater.")
print("new code has came.")
c=26
d=20
isgreater(c,d)
Gmean(c,d)
islesser(c,d)
if(c>d):
    print("first number is greater.")

else:
    print("second number is greater.")
#DEFAULT ARGUMENTS
def average(a=3,b=10):
   print("the average is ",((a+b)/2))

average(b=5)
def name(fname, mname="love",lname="paro"):
   print("your name is",fname,mname,lname)
name ("sumit",)
#KEYWORD ARGUMENTS--IN THIS ORDER DOSE note MATTER!
def average(a,b):
   print("the average is ",((a+b)/2))

average(b=5,a=10)
average(a=10,b=5)
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average of the numbers=",sum/len(numbers))

average(1,2,3,4,5,6,7,8,11)




