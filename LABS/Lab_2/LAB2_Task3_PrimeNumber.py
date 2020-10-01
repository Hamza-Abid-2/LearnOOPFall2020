#--------------------------------------------------------------------
# Taking a number from user and checking if it is Prime Number or not
#--------------------------------------------------------------------

EnteredNumber = int(input("Enter a Number: "))
print("-------------------")
if EnteredNumber > 1:
    primeNumber = EnteredNumber % 2
    if primeNumber == 0:
        print(EnteredNumber, "is not a Prime Number")
    else:
        print(EnteredNumber, "is a Prime Number")
else:
    print(EnteredNumber, "is not a Prime Number")