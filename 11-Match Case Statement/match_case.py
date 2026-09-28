num1 = int(input("Enter the Value of num1: "))
num2 = int(input("Enter the Value of num2: "))
choice = int(input("Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division: "))
match choice:
    case 1:
        print("Addition",num1+num2)
    case 2:
        print("Subtraction",num1-num2)
    case 3:
        print("Multiplication",num1*num2)
    case 4:
        print("Division",num1/num2)
    case _:
        print('Invalid Choice')
