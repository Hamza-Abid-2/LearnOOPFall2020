# Taking value from user at run time
# The value we enter using the input method is always of string type
# so if you wanted to perform any kind of mathematical operation you will have to convert it
# Changing or converting of data type is called type Casting
#--------------------------------------------------------------------------------------------

studenName = input("Enter Your Name: ")
studenAge = input("Enter Your Roll Number: ")
marksEng = int(input("Enter marks of English: "))         # Use int before bracket to show the mathematical value
marksMath = int(input("Enter marks of Maths: "))
marksUrdu = int(input("Enter marks of Urdu: "))
totalMarks = marksEng + marksMath + marksUrdu             # To Add the value of all subjects

print("==============================================")

print("Name: " )
print(studenName)
print("-----------------")
print("Roll Number: ")
print(studenAge)
print("-----------------")
print("Student total marks are: ")
print(totalMarks)
print("-----------------")






