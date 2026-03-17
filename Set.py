#Create a set of 5 fruits.
fruit={"apple","banana","lemmon","coconut","papaya"}

#Add 2 new fruits.
fruit.update(["mango","lichhi"])

#Remove one fruit.
fruit.discard("apple")

#Find common elements between two sets.
random={"apple","banana","mango","car","bike"}
print(fruit & random)

#Convert list [1,1,2,3,4,4,5] into unique list.
list=[1,1,2,3,4,4,5]
uniquelist=set(list)
print(uniquelist)

#Create a program that:
#Takes student names in two different classes
#Finds students in both classes
#Finds students only in first class

class1=set()
class2=set()
total1=int(input("how many students are there in class 1"))
for i in range(total1):
    name=input("\nEnter the name of student in class 1: ")
    class1.add(name)
total2=int(input("How many students are there in class 2"))
for i in range(total2):
    name=input("\n Enter the name of the student inn class 2: ")
    class2.add(name)
all_students=set(class1|class2)
print("All students= ",all_students)
only1=class1-class2
print("Students only in class1",only1)

#Create a menu-driven program:
#Add element, Remove element, Display set, Exit, 
menu=set()
while True:
    print("Enter  1 to add element.")
    print("Enter 2 to remove element")
    print("Enter 3 to see the set")
    print("Enter 4 to exit this")
    number=input("Enter the number: ")
    if number=="1":
        add=input("Enter the element to add: ")
        menu.add(add)
    elif number=="2":
        less=input("Enter the number to remove: ")
        menu.discard(less)
    elif number=="3":
        print(menu)
    elif number=="4":
        print("Exiting ........")
        break
    else:
        print("The number you entered is wrong!")            
            
