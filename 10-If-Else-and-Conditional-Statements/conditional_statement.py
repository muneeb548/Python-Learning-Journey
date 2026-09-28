#If_Else Practice
apple_price = 200
budget = 220
if(apple_price<=budget):
    print("Alexa, Add 1kg Apple to the CArt;")
else:
    print("Alexa, do not add Apple to the Cart:")

#ELIF_Statement Practice
num = int(input("Enter the value of num: "))
if(num<0):
    print("Number Is Negative: ")
elif(num==0):
    print("Number Is Zero: ")
elif(num==999):
    print("Number is Special")
else:
    print("Number Is Positive: ")

#Nested_If Staement Practice
num = 18
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num>=10):
        print("Number is Between 11-20: ")
    elif(num<=10):
        print("Number is between 1-10")
    else:
        print("Number is Greater than 20: ")
else:
    print("Number is Zero: ")
