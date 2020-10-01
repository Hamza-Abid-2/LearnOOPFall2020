#-------------------------------------------------------
# Taking number from user and check if it is Even or Odd
#-------------------------------------------------------

Number = int(input("Enter a value: "))
print("-----------------------------")
Value = Number % 2
if Value == 0:
    print(Number, "is an even value")
else:
    print(Number, "is an odd value")
print("======================================================")

#----------------------------------------------------------------------------------
# Taking range of number from the user to find  if it is Even or Odd using For Loop
#----------------------------------------------------------------------------------

startinLimit = int(input("Enter starting value: "))
UpperLimit = int(input("Enter end value: "))
print("-----------------------------")
for Numbers in range(startinLimit, UpperLimit + 1):
    Value = Numbers % 2
    if Value == 0:
        print(Numbers, "is an even")
    else:
        print(Numbers, "is an odd")
print("========================================================")

#------------------------------------------------------------------------------------
# Taking range of number from the user to find  if it is Even or Odd using While Loop
#------------------------------------------------------------------------------------

startinLimit = int(input("Enter starting value: "))
EndinLimit = int(input("Enter end value: "))
print("-----------------------------")
while (startinLimit <= EndinLimit):
    Value = startinLimit % 2
    if Value == 0:
        print(startinLimit, "is an even")
    else:
        print(startinLimit, "is an odd")
    startinLimit = startinLimit + 1
print("================================================================")

#---------------------------------------------------------------
# Finding total number of Even and Odd in range using For Loop
#---------------------------------------------------------------

startinLimit = int(input("Enter starting value: "))
EndinLimit = int(input("Enter end value: "))
print("-----------------------------")
EvenNumber = 0
OddNumber = 0
for Numbers in range (startinLimit, EndinLimit + 1):
    Value = Numbers % 2
    if Value == 0:
        EvenNumber = EvenNumber + 1
    else:
        OddNumber = OddNumber + 1
print ("Total number of even number is = ",EvenNumber)
print ("Total number of odd number is = ",OddNumber)
print("=================================================================")

#---------------------------------------------------------------
# Finding total number of Even and Odd in range using While Loop
#---------------------------------------------------------------

startinLimit = int(input("Enter starting value: "))
EndinLimit = int(input("Enter end value: "))
print("-----------------------------")
EvenNumber = 0
OddNumber = 0
while (startinLimit <= EndinLimit):
    Value = startinLimit % 2
    if Value== 0:
        EvenNumber = EvenNumber + 1
    else:
        OddNumber = OddNumber + 1

    startinLimit = startinLimit + 1
print ("Total number of even number is = ", EvenNumber)
print ("Total number of odd number is = ", OddNumber)

print("================== END ========================")





