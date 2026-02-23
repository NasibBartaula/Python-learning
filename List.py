#Create a list of 5 numbers and print it.
numbers = [10, 20, 30, 40, 50]
print(numbers)

#Add a new element to the end of a list.
numbers.append(60)
print(numbers)

#Insert an element at index 2.
numbers.insert(2, 25)
print(numbers)

#Remove an element using remove()
numbers.remove(25)
print(numbers)

#Remove an element using pop()
numbers.pop()  # removes last element
print(numbers)

#Find the length of a list.
print(len(numbers))

#Check if a number exists in a list.
print(30 in numbers)

#Print the first and last element of a list.
print(numbers[0])
print(numbers[-1])

#Reverse a list.
numbers.reverse()
print(numbers)

#Sort a list in ascending and descending order.
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#Count how many times a number appears in a list.
numbers.append(20)
print(numbers.count(20))

#Print all elements using a for loop.
print("All elements:")
for num in numbers:
    print(num)

#Print only even numbers from a list.
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

#Find the sum of all elements.
print(sum(numbers))

#Find the largest and smallest number.
print(max(numbers))
print(min(numbers))

#Create a new list with squares of each element.
squares = [num**2 for num in numbers]
print(squares)

#Remove duplicate elements from a list.
unique_numbers = list(set(numbers))
print(unique_numbers)

#Merge two lists.
list2 = [100, 200, 300]
merged = numbers + list2
print(merged)

#Find the second largest number.
unique_sorted = sorted(list(set(numbers)))
if len(unique_sorted) >= 2:
    print("Second largest:", unique_sorted[-2])

#Take 5 numbers as input from user and store in a list.
user_list = []
for i in range(5):
    num = int(input("Enter number: "))
    user_list.append(num)
print(user_list)

#Check if a list is palindrome.
if user_list == user_list[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#Rotate a list to the right by 1 position.
rotated = user_list[-1:] + user_list[:-1]
print(rotated)

#Split a list into even and odd lists.
even_list = []
odd_list = []

for num in user_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list)
print(odd_list)

#Find common elements between two lists.
listA = [1, 2, 3, 4, 5]
listB = [4, 5, 6, 7, 8]

common = list(set(listA) & set(listB))
print(common)

#Flatten this list: [[1,2],[3,4],[5,6]]
nested = [[1,2],[3,4],[5,6]]
all=[]
for sublist in nested:
    for n in sublist:
        all.append(n)
print(all)        