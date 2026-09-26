# Strings are Immutable
# A string cannot be changed directly after it is created.

a = "Raja Muneeb Ahmed!!!!"

# Finding the length of the string
print(len(a))

# Printing the original string
print(a)

# Converting the string into uppercase
print(a.upper())

# Converting the string into lowercase
print(a.lower())

# Removing exclamation marks from the right side
print(a.rstrip("!"))

# Replacing a part of the string with another value
print(a.replace("Raja Muneeb Ahmed", "Raju Bahia"))

# Splitting the string into a list using space
print(a.split(" "))

# Capitalize Method
# Converts the first character to uppercase
BlogHeading = "introduction to Python"
print(BlogHeading.capitalize())

# Center Method
# Finds the length of the string
str1 = "Welcome to the console"
print(len(str1))
# Centers the string within the given width
print(str1.center(30))

# Count Method
# Counts how many times "Raja" appears in the string
print(a.count("Raja"))

# Endswith Method
# Checks whether the string ends with "!!!"
str2 = "Welcome to the console!!!"
print(str2.endswith("!!!"))

# Find Method
# Finds the index of the first occurrence of "is"
str1 = "He's name is raja. He is very honest person."
print(str1.find("is"))

# Isalnum Method
# Checks whether the string contains only letters and numbers
str2 = "Welcome to the console!!!"
print(str2.isalnum())

# Isalpha Method
# Checks whether the string contains only alphabetic characters
str2 = "Welcometotheconsole"
print(str2.isalpha())

# Islower Method
# Checks whether all alphabetic characters are lowercase
str2 = "hello world"
print(str2.islower())

# Isprintable Method
# Checks whether all characters in the string are printable
print(str2.isprintable())

# Isspace Method
# Checks whether the string contains only whitespace characters
str3 = "    "
print(str3.isspace())

# Istitle Method
# Checks whether each word starts with an uppercase letter
str3 = "World Health Organization"
print(str3.istitle())

# Istitle Method Example
# This returns False because "health" starts with a lowercase letter
str3 = "World health Organization"
print(str3.istitle())

# Swapcase Method
# Converts uppercase letters to lowercase and lowercase letters to uppercase
print(str3.swapcase())

# Title Method
# Converts the first letter of each word to uppercase
str1 = "his name is raja"
print(str1.title())
