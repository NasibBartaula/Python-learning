#Write a program to find:
# Maximum value
# Minimum value
marks=(23,34,45,56)
lowest  =min(marks)
highest =max(marks)
print(lowest)
print(highest)

# Reverse a tuple:

rev=marks[::-1]
print(rev)

#Concatenate two tuples.
joint=marks+rev
print(joint)

#Slice a tuple and print only even index elements.
even_index=joint[::2]
print(even_index)

#Swap two tuples.
marks,joint=joint,marks
print("marks",marks)
print("joint",joint)