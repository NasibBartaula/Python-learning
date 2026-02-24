#Countries & Capitals . Print All Capitals
countries = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "USA": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris"
}
for capital in countries.values():
    print(capital)

#Update, Add, Remove
student = {"name": "Ram", "age": 20, "grade": "A"}

# Update age
student["age"] = 21

# Add new
student["city"] = "Kathmandu"

# Remove grade
student.pop("grade")

print(student)

#Check if Key Exists
data = {"name": "Nasib", "age": 20}
key = "age"

if key in data:
    print("Key exists")
else:
    print("Key does not exist")

#Count Number of Keys
data = {"a": 1, "b": 2, "c": 3}
print(len(data))

#Print All Keys and Values
data = {"name": "Nasib", "age": 20, "course": "BCA"}
for key, value in data.items():
    print(key, ":", value)

#Total & Average Marks
marks = {
    "Math": 80,
    "English": 75,
    "Science": 90
}

total = sum(marks.values())
average = total / len(marks)
print(total)
print(average)

#Find Highest Value
marks = {"Math": 80, "English": 75, "Science": 90}

highest = max(marks.values())
print(highest)

highest_subject = max(marks, key=marks.get)
print("Highest:", highest_subject, marks[highest_subject])

#Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combine = dict1 | dict2  
print(combine)

#Convert Two Lists into Dictionary
a = ["name", "age", "course"]
b = ["Nasib", 20, "BCA"]
result = dict(zip(a, b))
print(result)