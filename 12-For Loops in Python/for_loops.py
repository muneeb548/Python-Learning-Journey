# For Loop Practice with List and If-Else
marks = [45, 78, 32, 90, 66]

for i in marks:

    if i >= 40:
        print(i, "Pass")

    else:
        print(i, "Fail")


# For Loop with range()
# Prints numbers from 1 to 10
for i in range(1, 11):
    print(i)


# For Loop with range() and Step
# Prints odd numbers from 1 to 10
for i in range(1, 11, 2):
    print(i)


# For Loop with range() and If Statement
# Prints even numbers from 2 to 20
for i in range(2, 21):

    if i % 2 == 0:
        print(i)


# Reverse Counting using range()
# Prints numbers from 10 down to 1
for i in range(10, 0, -1):
    print(i)


# Iterating Through a String
# Prints each character of the string separately
name = "RAJA MUNEEB:"

for i in name:
    print(i)


# Iterating Through a List
# Prints each fruit separately
fruits = ["Apple", "Banana", "Mango", "Orange"]

for i in fruits:
    print(i)


# For Loop with List and If-Else
# Checks whether each number is 20 or greater
numbers = [10, 15, 20, 25, 30]

for i in numbers:

    if i >= 20:
        print(i, "Bigger Number")

    else:
        print(i, "Smaller Number")


# Using break in a For Loop
# Stops the loop when the number reaches 30
numbers = [10, 20, 30, 40, 50]

for i in numbers:

    print(i)

    if i == 30:
        break


# Using continue in a For Loop
# Skips the number 5 and continues the loop
for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# Using For Loop with If Statement on a String
# Prints only the letter 'e' from the string
name = "Muneeb:"

for i in name:

    if i == "e":
        print(i)
