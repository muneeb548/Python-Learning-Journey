# Student Profile Analyzer - Part 1, Part 2 & Part 3

# Taking Student Information
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
city = input("Enter your City: ")
cgpa = float(input("Enter your CGPA: "))
language = input("Enter your Favourite Programming Language: ")

# Student Profile
print("\n==========================")
print("      Student Profile")
print("==========================")

print("Name:", name.strip().title())
print("Age:", age)
print("City:", city.strip().title())
print("CGPA:", cgpa)
print("Favourite Language:", language.strip().title())

# String Analysis
print("\n--- String Analysis ---")

print("Clean Name:", name.strip())
print("Formatted Name:", name.strip().title())
print("Formatted City:", city.strip().title())
print("Language in Uppercase:", language.upper())
print("Name Length:", len(name))
print("Position of 'a':", name.find("a"))
print("Name is Alphabetic:", name.isalpha())

# Eligibility Check
print("\n--- Eligibility Check ---")

if cgpa >= 2.5 and age >= 18:
    print("Status: Eligible")
else:
    print("Status: Not Eligible")

# CGPA Performance
if cgpa >= 3.0:
    print("Performance: Excellent CGPA")
else:
    print("Performance: Good Effort")


# In this task, I practiced:
# 1. Taking user input
# 2. Type casting using int() and float()
# 3. Variables and different data types
# 4. print() function
# 5. Escape sequence \n
# 6. String methods: strip(), title(), upper()
# 7. len(), find() and isalpha()
# 8. Comparison operators
# 9. Logical operator 'and'
# 10. if-else conditions
# 11. Eligibility checking
# 12. Basic CGPA performance checking
