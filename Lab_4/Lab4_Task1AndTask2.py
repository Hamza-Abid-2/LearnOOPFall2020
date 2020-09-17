

# Task 1 -  Creat University and Teacher Class
# -------------------------------------
class university:
    uniName = ""
    uniCity = ""
    uniAge = ""

    def universityInformation(self):  # Function
        print("University Name: " + self.uniName)
        print("City: " + self.uniCity)
        print("Years in service: " + str(self.uniAge) + "years ")
        print("-----------------------------------")

class teacher:
    tchName = ""
    tchSubject = ""
    tchsal = ""

    def teacherintroduction(self):
        print("teacher Name: " + self.tchName)
        print("Teacher Subject: " + self.tchSubject)
        print("Teacher Salary: " + str(self.tchsal))
        print("------------------------------------")


# ------------------------------------------------------------------------------------
#  Task 2 - creat objects and apply loop
#-------------------------------------------------------------------------------------
# Creating objects of:
# university class

uni1 = university()
uni1.uniName = "Superior University"
uni1.uniCity = "Lahore , Raiwand"
uni1.uniAge = "20"

uni2 = university()
uni2.uniName = "Bahria university"
uni2.uniCity = "Lahore , Johar Town"
uni2.uniAge = "15"

uni3 = university()
uni3.uniName = "GC University"
uni3.uniCity = "Lahore , Anarkali "
uni3.uniAge = "50"

uni4 = university()
uni4.uniName = "punjab University"
uni4.uniCity = "Lahore , canal road"
uni4.uniAge = "40"

uni5 = university()
uni5.uniName = "Hajvery University"
uni5.uniCity = "Lahore , Gulberg"
uni5.uniAge = "25"

# Teacher Class

tch1 = teacher()
tch1.tchName = "Prof.Ahmad"
tch1.tchSubject = "Math"
tch1.tchsal = "50000"

tch2 = teacher()
tch2.tchName = "Prof.Qasim"
tch2.tchSubject = "Object Oriented Programming "
tch2.tchsal = "60000"

tch3 = teacher()
tch3.tchName = "Prof.Usama"
tch3.tchSubject = "Linear Algebra"
tch3.tchsal = "70000"

tch4 = teacher()
tch4.tchName = "Miss Nausheen"
tch4.tchSubject = "Technical and Business writing"
tch4.tchsal = "65000"

tch5 = teacher()
tch5.tchName = "Prof,Saleem"
tch5.tchSubject = "Statistics"
tch5.tchsal = "55000"

# Creating list and applying FOR loop

uniList = [uni1, uni2, uni3, uni4, uni5]
for eachUni in uniList:
    eachUni.universityInformation()


teacherList = [tch1, tch2, tch3, tch4, tch5]
for eachTeacher in teacherList:
    eachTeacher.teacherintroduction()

# --------------------------- END -------------------------------------










