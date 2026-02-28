#Write a function to check if a number is even or odd.
def check(number):
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
n=int(input("Enter the number: "))
check(n)

#Write a function to calculate factorial.
def factorial(number):
    if number <=1:
        return 1
    n=number*factorial(number-1)
    return n
b=int(input("Enter the number to find factorial of"))
b=factorial(b)
print(b)

#Write a function that returns the largest of 3 numbers.
def largest(a,b,c):
    if a>b&a>c:
        return a
    elif b>a&b>c:
        return b
    else:
        return c
    
a=int(input("Enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number"))
great=largest(a,b,c)
print(great)

#Create a simple calculator using functions (add, subtract, multiply, divide).
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b 
code=int(input("Enter 1 to add,2 to subtract ,3 to multiply and 4 to divide"))
if code==1:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(add(a,b))
elif code==2:
    a=int(input("Enter the number to be subtracted: "))
    b=int(input("Enter the Subtrahend"))
    print(sub(a,b))
elif code==3:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(multiply(a,b))
elif code==4:
    a=int(input("Enter the first divident: "))
    b=int(input("Enter the second divider: "))
    print(divide(a,b))    

#Create a  list where values are squares of 1 to 30.
def list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
list()
            
#Create a function to check the number is prime or not
def prime(num):
    if num ==1:
        print("The number is not prime")
    elif num==2:
        print("The number is prime")
    if num>2:
        for i in range(2,num):
             if num%i==0:
                 print("The number is not a prime number")
                 break 
        else:
            print("The number is a prime number")

num=int(input("Enter the number to be checked as a prime"))
prime(num)                     