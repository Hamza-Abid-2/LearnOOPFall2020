# Function OverRiding
# function with same name present in parent class is also present in child class
# But with different implementation

class parent:
    fatherName = ""
    motherName = ""
    def motorcycle(self):
        print("This is " + str(self.fatherName) + "motorcycle")
        print("This is Father's motorcycle with simple horn")


class child(parent):
    childName = ""
    childAge = ""
    def motorcycle(self):
       print("This is " + str(self.childName) + "motorcycle")
       print("This is child own motorcycle with loud horn and heavy silencer")

c1 = child()
c1.childName = "hamza"
c1.childAge = "20"
c1.fatherName = "ahmad"
c1.motherName = "amna"
c1.motorcycle()
