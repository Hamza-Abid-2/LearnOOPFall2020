# Multiplication table using Loops
#-------------------------------------------------------
#                      For Loop
# ------------------------------------------------------

print("Table using -> For Loop")
print("-----------------------")
number = int(input("enter table number : "))
LowerRange = int(input("enter the Lower range : "))
UpperRange = int(input("enter the Upper range : "))

for LowerRange in range(LowerRange , UpperRange):
    Answer = number * LowerRange
    print(number ,"*",LowerRange, "=", Answer)

print("==========================================================")

#-----------------------------------------------------------------
#                         While Loop
#-----------------------------------------------------------------

print("Table using -> While Loop")
print("-------------------------")
number = int(input("Enter table number : "))
LowerRange = int(input("Enter the lower range : "))
UpperRange = int(input("Enter the upper range : "))

while LowerRange <= UpperRange :
    Answer = number * LowerRange
    print(number ,"*",LowerRange, "=", Answer)
    LowerRange += 1