# Variables and Data Types

Today I learned about Variables and Data Types in Python.

## Variables

A variable is a name used to store a value in Python. The value stored in a variable can be different types of data, such as a number, text, or Boolean value.

Example:

```python
name = "Raja Muneeb"
age = 22
```

Here, `name` stores text and `age` stores a number.

## Data Types

Data types tell us what type of data is stored in a variable.

Python has different built-in data types.

### 1. Numeric Data

Numeric data is used to store numbers. It includes:

- `int` → Used for whole numbers.
- `float` → Used for decimal numbers.
- `complex` → Used for complex numbers.

Examples:

```python
a = 10          # int
b = 10.5        # float
c = complex(8,9) # complex
```

### 2. Text Data - `str`

`str` stands for string. It is used to store text or a sequence of characters.

Example:

```python
name = "Raja Muneeb"
```

### 3. Boolean Data - `bool`

Boolean data represents one of two values:

- `True`
- `False`

It is commonly used when something has only two possible conditions.

Example:

```python
is_student = True
```

### 4. None Data - `None`

`None` represents the absence of a value. It means that a variable currently has no value.

Example:

```python
d = None
```

### 5. Sequence Data

Sequence data is used to store multiple values in an ordered way.

It includes `list` and `tuple`.

#### List

A list is an ordered collection of items. A list can contain different types of values and can also contain another list.

Example:

```python
List1 = [1, 45, ["apple", "banana"]]
print(List1)
```

#### Tuple

A tuple is also an ordered collection of items. It can contain multiple values.

Example:

```python
tuple1 = (1, 45, ("apple", "banana"))
print(tuple1)
```

### 6. Mapped Data - `dict`

A dictionary (`dict`) stores data in **key-value pairs**. Each key is used to access its related value.

Example:

```python
dict1 = {
    "name": "Muneeb",
    "age": 22,
    "Gender": "Boy"
}

print(dict1)
```

## Checking Data Types

We can use the `type()` function to check the data type of a variable.

Example:

```python
a = 1
b = True
c = "Raja"
d = None
e = complex(8, 9)

print("The type of a is", type(a))
print("The type of b is", type(b))
print("The type of c is", type(c))
print("The type of d is", type(d))
print("The type of e is", type(e))
```

## What I Practiced

Today I practiced:

- Creating variables
- Storing different types of values
- Using `int`, `float`, and `complex`
- Using `str` and Boolean values
- Using `None`
- Creating lists and tuples
- Creating dictionaries
- Checking data types using `type()`
- Performing calculations with variables

## What I Learned Today

Today I learned about variables and built-in data types in Python. I also practiced different types of data such as numeric, text, Boolean, sequence and mapped data.
