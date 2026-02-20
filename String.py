"""A="Function in string"

#length
print(len(A))

#To find the number of times character is occuring
print(A.count("n"))

#To convert each letter into uppercase and lowercase
print(A.upper())
print(A.lower())

#To find index of any character
print(A.index("i",10,18))
print(A.find("i",10,18)) 

#To convert the first letter to capital     
print(A.capitalize())  
print(A.casefold())

#To write variables inside a string
name="Nasib"
sentence="My name is {}"
print(sentence.format(name))

#Centralize a string
print(name.center(20))

#isalnum
a="Apple"
b="555"
c="This is great"
d="44Na#$"

print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

#isalpha
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())

#isdecimal
print(a.isdecimal())
print(b.isdecimal())
print(c.isdecimal())
print(d.isdecimal())

#islower #isupper #isspace#
print(a,a.islower())
print(a,a.isupper())
print(a,a.isspace())"""

#Take an input from the uesr then reverse it
print("Reversing the string")
string=input("Enter the string: ")
print(string[::-1])

#To check entered string conatins only numbers
print("digit cheaker")
a=input("Enter the string")
b=a.isdigit()
if b=="True":
    print("The string contains only digit")
else:
    print("The number doesnot contain only digit")    

#To check if the string is palindrome
print("To check if the string is palindrome or not")
c=input("Enter the string")
d=c[::-1]
if c==d:
    print("The number is palindrome")
else:
    print("feThe number is not palindrome")    

#To find voewls in a string
print("Vowel finder")
e=input("Enter the string")
vowels=0
for i in e:
    if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
        vowels+=1
print(vowels)      