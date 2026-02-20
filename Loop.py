#Find sum of first 10 odd number
print("Sum of first 10 odd numbers")
for i in range(1,21,2):
    print(i)

# Ask the user to enter numbers until they type 0, then print the sum of all entered numbers using a while loop.
print("Adding the numbers until user enters zero")
sum=0
while True:
    i=int(input("Enter the nunber"))
    sum+=i
    if i==0:
        print(f"The sum is {sum}")
        break

#Print numbers 1–10, but skip 5 using continue.
print("print number 1-10 without 5")
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)

#Print multiplication table up to 10.
i=1
while(i<10):
    j=1
    while(j<10):
        print(i,"X",j,"=",i*j)

        j+=1
    print(" ")    
    i+=1    

#Print this number pattern using nested for loops:
1
12
123
1234
12345
print("Pattern")
for i in range(1,6):
    j=1
    while(j<=i):
        print(j,end="")
        j+=1
    print("")   

#Billing system at supermarket
print("Billing system at supermarket")
while True:
    Name=input("Enter the name of the costomer")
    total=0
    while True:
        quantity=int(input("Enter the quantity"))
        amount=int(input("Enter the amount for the product"))
        total+=quantity*amount
        repeat=input("Any other products? Press y for yes and n for no")
        if(repeat=="n"):
            break
    print(f"Hello {Name}!! Thank you for visiting us. your total bill is of {total}")
    repeat1=input("Is this your last costomer of the day?Press y for yes and n for no")
    if (repeat1=="y"):
        break

#To reverse a number
print("Reversing the number")
num=int(input("Enter the number"))
reverse=0
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(f"Reverse number is {reverse}")   

#Check if number is palindrome                                         
num=int(input("Enter the number"))
original=num
reverse=0
while num!=0:
    digit=num//10
    reverse=reverse*10+digit
    num=num/10
if(original==reverse):
    print("The number is palindrome")
else:
    print("The number is not palindrome")

#Factorial using loop
print("Factorial finder")
num=int(input("Enter the number"))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print(f"The factorial is {fact}")

#sum of digit of a number
print("Sum of digit of a number")
num=int(input("Enter the number"))
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
print(f"The sum of the digit is {sum}")    

#Password checker
print("Password checker")
password="Nasib123"
attempt=3
while attempt>0:
    password_=input("Enter the password")
    if (password_==password):
        print("Access granted")
        break
    else:
        attempt-=1    
if (attempt==0):
    print("account locked")