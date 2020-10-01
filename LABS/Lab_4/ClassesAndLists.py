# in this lecture we will learn how to use list in classes
# How can we get and store in them
# What is difference between the list in class or list of objects of class outside the class
# Creating a human Class
class human:
    name = ""   # Attributes / Variable
    age = ""

    def introduction(self):      #Behaviour / Functions
        print("My name is: " + self.name)
        print("My age is: " + str(self.age) + "years")
        print("-------------------------------------------")

# Creating objects of class human
h1 = human()
h1.name = "Hamza"
h1.age = "20"
h1.introduction()

h2 = human()
h2.name = "hassan"
h2.age = "19"
h2.introduction()

#---------------------------------------------------------------

# Creating a class student - which include a list of student marks
class student:
    stdName = ""
    stdAge = ""
    stdMarks = []

    def introduction(self):
        print("My name is: " + self.stdName)
        print("My age is: " + self.stdAge + " years")
        print("My marks in Maths are: " + str(self.stdMarks[0]))
        print("My marks in english are: " + str(self.stdMarks[1]))
        print("My marks in Urdu are: " + str(self.stdMarks[2]))
        print("-------------------------------------")

# creating Objects of student class
std1 = student()
std1.stdName = "Hamza"
std1.stdAge = "20"
std1.stdMarks = [21, 30, 45]
std1.introduction()

std2 = student()
std2.stdName = "hassan"
std2.stdAge = "19"
std2.stdMarks = [50, 45, 49]
std2.introduction()

std3 = student()
std3.stdName = "Usama"
std3.stdAge = "22"
std3.stdMarks = [15, 35, 42]
std3.introduction()

# Creating list

studentList = [std1, std2, std3]
studentList[2].introduction()

