# To input 2 numbers and print their sum
print("Sum finder")
First_num =  int(input("Enter the first number: "))
Second_num=  int(input("Enter the second number: "))
print("The sum is ",First_num + Second_num)


    # To input side of a square and pront it's area
print("Area finder of a square")
side=float(input("Enter the side of a square"))
print("The area of the square is ",side * side)

# To input 2 floating point number and pront their average
print("Average finder of 2 floating point numbers")
First_float =float(input("Enter the first number"))
Second_float=float(input("ENter the second number"))
average=(First_float+Second_float)/2
print("The average is ",average)

# If the number is positive negative or zero
print("Positive , Negative and Zero checker")
num=float(input("Enter the number"))
if(num<0):
    print("THe number is negative")
elif(num>0):
    print("The number is positive")
else:
    print("The number is zero")       

#To input users name and print its length and find occorancve of "$" 
print("String length and $ occorance finder ")
name=input("Enter your name")
length=len(name)
print("The length is ",length)
times=name.find("$")
print("The occorance of $ is ",times)

# If a letter is Vowel or Consonant
print("Vowel or consonent finder")
letter=input("Enter the letter")
if letter.lower() in ["a","e","i","o","u"]:
    print("The letter is vowel")
else:
    print("The letter is consunant")\

# To check if the number is odd or even
print("Odd or Even checker")
n=int(input("Enter the number"))
if(n%2==0):
    print("The number is even")
else:
    print("The number is odd")

# To check the number is multiple of 7 or not
print("To check the number is multiply of 7 or not")
number=int(input("Enter the number"))
if(number%7==0):
    print("The number is multiple of seven")
else:
    print("The number is not multiple of seven")

# To print the number of digit entered
print("The number of digit entered counter")
a=input("Enter the number")
digit=len(a)
print("The number of digit entered is ",digit)

# To grade the marks
print("Grade calculator")
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B+")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Multiplication table generator
print("Multiplication table generator")
number=int(input("Enter the number"))

for i in range(1,11):
    print(number,"X",number,"=",number*i)