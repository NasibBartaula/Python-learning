#Create a datetime object for your birth date and:
#Print whether it is AM or PM
#Print minutes
#Print full weekday name
#Print full month name
import datetime
y = datetime.datetime(2005,1,29)
print(y.strftime("%p"))
print(y.strftime("%M"))
print(y.strftime("%A"))
print(y.strftime("%B"))

#Print current date and time using datetime module
b = datetime.datetime.now()
print(b)


#Generate a random number between 1 and 1000
import random
x = random.randint(1,1000)
print(x)

#Simulate a coin toss using random.choice()
a = ["heads","tails"]
b = random.choice(a)
print(b)

#Find maximum and minimum values from given numbers
import math
x = max(12,23,34)
print("The maximim value is ",x)

y = min(12,23,45)
print("The minimum value is ",y)

#Find power of a number (2^3)
x = pow(2,3)
print(x)

#Find square root of 49 using math module
b = math.sqrt(49)
print(b)

# 8️⃣ Find absolute value of -12
c = abs(-12)
print(c)

#Use ceil() to round 3.6 upward
k = math.ceil(3.6)
print(k)    

#Use floor() to round 3.4 downward
k = math.floor(3.4)
print(k)

#Own module
import Calculator
c=Calculator.add(3,7)
print(c)

d=Calculator.mul(2,6)
print(d)

e=Calculator.div(55,5)
print(e)