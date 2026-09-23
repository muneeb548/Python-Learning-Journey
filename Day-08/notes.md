# Day 08 - Taking User Input in Python

Today I learned how to take user input in Python using the `input()` function.

## Taking User Input

In Python, we can take user input directly by using the `input()` function.

The `input()` function takes input from the user and returns the value as a **string**.

### Syntax

```python
variable = input()
```

We can also display a message to the user while taking input:

```python
variable = input("Enter your name: ")
```

This will display the message and wait for the user to enter a value.

## Storing User Input in a Variable

We can store the value entered by the user in a variable.

Example:

```python
name = input("Enter your name: ")
print("My name is", name)
```

If the user enters `Muneeb`, the output will be:

```text
My name is Muneeb
```

## Input Returns a String

The `input()` function always returns the user input as a **string**.

For example:

```python
x = input("Enter first number: ")
y = input("Enter second number: ")

print(x + y)
```

If the user enters:

```text
5
10
```

The output will be:

```text
510
```

This happens because `x` and `y` are strings, so `+` joins them together instead of adding them as numbers.

## Type Casting User Input

If we want to use the input as another data type, we need to convert it using **type casting**.

For example, we can convert the input into an integer using `int()`.

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x + y)
```

If the user enters:

```text
5
10
```

The output will be:

```text
15
```

Here, `int()` converts the string input into an integer.

### Another Example

We can also convert input separately:

```python
x = input("Enter first number: ")
y = input("Enter second number: ")

print(x + y)
print(int(x) + int(y))
```

The first `print()` joins the two strings, while the second `print()` converts them into integers and performs addition.

## Important Point

The correct way to take an integer input directly is:

```python
variable = int(input("Enter a number: "))
```

**Not:**

```python
variable = int(input)
```

Because `input` without `()` refers to the function itself. We need to call the function using `input()` first.

## What I Learned Today

Today I learned how to take user input using the `input()` function.

I learned that `input()` returns the entered value as a string. I also learned how to display a message while taking input and how to convert string input into integers using `int()`.

I practiced taking numbers from the user and performing addition after converting them into integers.
