# String Methods in Python

Today I learned about different methods that can be used with strings in Python.

## Strings are Immutable

Strings in Python are **immutable**. This means that once a string is created, its original value cannot be changed directly.

String methods return a new string instead of changing the original string.

Example:

```python
a = "Raja Muneeb Ahmed!!!!"

print(a)
print(a.upper())
print(a)
```

The `upper()` method creates and returns a new string. The original string remains unchanged.

---

## 1. `upper()`

The `upper()` method converts all letters of a string into uppercase.

Example:

```python
a = "Raja Muneeb Ahmed"

print(a.upper())
```

Output:

```text
RAJA MUNEEB AHMED
```

---

## 2. `lower()`

The `lower()` method converts all letters of a string into lowercase.

Example:

```python
a = "Raja Muneeb Ahmed"

print(a.lower())
```

Output:

```text
raja muneeb ahmed
```

---

## 3. `rstrip()`

The `rstrip()` method removes specified characters from the right side of a string.

Example:

```python
a = "Raja Muneeb Ahmed!!!!"

print(a.rstrip("!"))
```

Output:

```text
Raja Muneeb Ahmed
```

---

## 4. `replace()`

The `replace()` method replaces a specified part of a string with another value.

Example:

```python
a = "Raja Muneeb Ahmed"

print(a.replace("Raja Muneeb Ahmed", "Raju Bahia"))
```

Output:

```text
Raju Bahia
```

---

## 5. `split()`

The `split()` method splits a string into a list.

Example:

```python
a = "Raja Muneeb Ahmed"

print(a.split(" "))
```

Output:

```text
['Raja', 'Muneeb', 'Ahmed']
```

Here, the string is split at each space.

---

## 6. `capitalize()`

The `capitalize()` method converts the first character of a string to uppercase and the remaining characters to lowercase.

Example:

```python
BlogHeading = "introduction to Python"

print(BlogHeading.capitalize())
```

Output:

```text
Introduction to python
```

---

## 7. `center()`

The `center()` method places a string in the center of a specified width.

Example:

```python
str1 = "Welcome to the console"

print(str1.center(30))
```

The string is centered within a total width of 30 characters.

---

## 8. `count()`

The `count()` method counts how many times a specified value appears in a string.

Example:

```python
a = "Raja Muneeb Ahmed!!!!"

print(a.count("Raja"))
```

Output:

```text
1
```

---

## 9. `endswith()`

The `endswith()` method checks whether a string ends with a specified value.

It returns `True` or `False`.

Example:

```python
str2 = "Welcome to the console!!!"

print(str2.endswith("!!!"))
```

Output:

```text
True
```

---

## 10. `find()`

The `find()` method searches for a specified value and returns its index.

If the value is not found, it returns `-1`.

Example:

```python
str1 = "He's name is raja. He is very honest person."

print(str1.find("is"))
```

Output:

```text
9
```

---

## 11. `isalnum()`

The `isalnum()` method returns `True` if all characters in the string are letters or numbers.

It returns `False` if the string contains spaces or special characters.

Example:

```python
str2 = "WelcomeToTheConsole123"

print(str2.isalnum())
```

Output:

```text
True
```

---

## 12. `isalpha()`

The `isalpha()` method returns `True` if all characters in the string are alphabetic letters.

It returns `False` if the string contains numbers, spaces, or special characters.

Example:

```python
str2 = "Welcometotheconsole"

print(str2.isalpha())
```

Output:

```text
True
```

---

## 13. `islower()`

The `islower()` method returns `True` if all alphabetic characters in the string are lowercase.

Example:

```python
str2 = "hello world"

print(str2.islower())
```

Output:

```text
True
```

---

## 14. `isprintable()`

The `isprintable()` method returns `True` if all characters in the string are printable.

Example:

```python
str2 = "Hello World"

print(str2.isprintable())
```

Output:

```text
True
```

---

## 15. `isspace()`

The `isspace()` method returns `True` if the string contains only whitespace characters such as spaces, tabs, or new lines.

Example:

```python
str3 = "    "

print(str3.isspace())
```

Output:

```text
True
```

---

## 16. `istitle()`

The `istitle()` method returns `True` if each word starts with an uppercase letter and the remaining letters are lowercase.

Example:

```python
str3 = "World Health Organization"

print(str3.istitle())
```

Output:

```text
True
```

Another example:

```python
str3 = "World health Organization"

print(str3.istitle())
```

Output:

```text
False
```

---

## 17. `swapcase()`

The `swapcase()` method changes uppercase letters to lowercase and lowercase letters to uppercase.

Example:

```python
str3 = "World health Organization"

print(str3.swapcase())
```

Output:

```text
wORLD HEALTH oRGANIZATION
```

---

## 18. `title()`

The `title()` method converts the first letter of each word to uppercase.

Example:

```python
str1 = "his name is raja"

print(str1.title())
```

Output:

```text
His Name Is Raja
```

---

## What I Learned Today

Today I learned about different string methods in Python.

I practiced:

* `upper()`
* `lower()`
* `rstrip()`
* `replace()`
* `split()`
* `capitalize()`
* `center()`
* `count()`
* `endswith()`
* `find()`
* `isalnum()`
* `isalpha()`
* `islower()`
* `isprintable()`
* `isspace()`
* `istitle()`
* `swapcase()`
* `title()`

I also learned that strings are **immutable**, which means their original value cannot be changed directly.
