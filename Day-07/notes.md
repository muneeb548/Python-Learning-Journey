# Day 07 - Type Casting

Today I learned about Type Casting and Type Conversion in Python.

## What is Type Casting?

The conversion of one data type into another data type is known as **Type Casting** or **Type Conversion** in Python.

For example, we can convert a string into an integer using `int()`.

```python
a = "1"
b = "3"

print(int(a) + int(b))
```

Output:

```text
4
```

Here, `"1"` and `"3"` are strings, but `int()` converts them into integers before addition.

## Types of Type Casting

There are two main types of type casting in Python:

1. Explicit Type Casting
2. Implicit Type Casting

## 1. Explicit Type Casting

The conversion of one data type into another data type **manually by the developer** with the help of Python's built-in type conversion functions is known as **Explicit Type Casting**.

In explicit type casting, we tell Python which data type we want.

### Example of Explicit Type Casting

```python
string = "15"
number = 7

string_number = int(string)

sum = number + string_number

print("The sum of both the numbers is", sum)
```

Output:

```text
The sum of both the numbers is 22
```

Here:

- `string = "15"` is a string.
- `int(string)` converts the string `"15"` into an integer `15`.
- Then `15` is added to `7`.

Some commonly used type conversion functions are:

- `int()` → Converts a value into an integer.
- `float()` → Converts a value into a float.
- `str()` → Converts a value into a string.

Example:

```python
a = "10"

print(int(a))
print(float(a))
print(str(10))
```

## 2. Implicit Type Casting

Python can automatically convert a smaller data type into a higher data type to prevent data loss. This is known as **Implicit Type Casting**.

In implicit type casting, Python automatically converts the data type without us manually converting it.

### Example of Implicit Type Casting

```python
c = 7
print(type(c))

d = 8.0
print(type(d))

result = c + d

print(result)
print(type(result))
```

Output:

```text
<class 'int'>
<class 'float'>
15.0
<class 'float'>
```

Here:

- `c` is an `int`.
- `d` is a `float`.
- When we add `int` and `float`, Python automatically converts the integer into a float.
- The result is `15.0`, which is a `float`.

## Explicit vs Implicit Type Casting

| Type | Meaning |
|---|---|
| Explicit Type Casting | Developer manually converts one data type into another. |
| Implicit Type Casting | Python automatically converts the data type when needed. |

### Simple Example

**Explicit:**

```python
a = "5"
b = int(a)
```

Here, we manually converted a string into an integer.

**Implicit:**

```python
a = 5
b = 2.5

result = a + b
```

Here, Python automatically converts the integer into a float.

## What I Learned Today

Today I learned about Type Casting and Type Conversion in Python.

I learned that type casting is used to convert one data type into another. I also learned about **Explicit Type Casting**, where the developer manually converts the data type, and **Implicit Type Casting**, where Python automatically converts the data type.

I also practiced `int()`, `float()`, `str()` and `type()` functions.
