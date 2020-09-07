

print("--------------- Calculator ---------------")
num1 = float(input("Enter Number 1: "))
Operator = input("Enter Operator +, -, * ,/: ")
num2 = float(input("Enter Number 2: "))
#Operator = input("Enter Operator +, -, * ,/: ")

if Operator == "+":
    print(num1 + num2)

elif Operator == "-":
    print(num1 - num2)

elif Operator == "*":
    print(num1 * num2)

elif Operator == "/":
    print(num1 / num2)

else:
    print("....ERROR....\tEnter the correct Operator")
