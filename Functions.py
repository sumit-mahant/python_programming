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
    return sum/len(numbers)

c=average(1,2,3,4,5,6,7,8)
print(c)
#RECURSION
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))
print(factorial(4))
#FIBONACHI SERIES
def fibonacci(n):
 if(n<=1):
      return n
 else:
    return fibonacci(n-1)+fibonacci(n-2) 
for i in range(10):
   print(fibonacci(i))
n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series using loop:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

z="sumit"



    
    
  
 




