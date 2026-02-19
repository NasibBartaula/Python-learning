A="Function in string"

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
print(a,a.isspace())
