# Operators

Today I learned about Operators in Python.

## What are Operators?

Operators are symbols that are used to perform different operations on values and variables.

Example:

```python
a = 10
b = 5

print(a + b)
```

Here, `+` is an operator used for addition.

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulus | `10 % 3` |
| `//` | Floor Division | `10 // 3` |
| `**` | Exponentiation | `2 ** 3` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

### Modulus `%`

The modulus operator gives the remainder after division.

Example:

```python
print(10 % 3)
```

Output:

```text
1
```

### Floor Division `//`

Floor division gives the quotient without the decimal part.

Example:

```python
print(10 // 3)
```

Output:

```text
3
```

### Exponentiation `**`

Exponentiation is used to calculate the power of a number.

Example:

```python
print(2 ** 3)
```

Output:

```text
8
```

## 2. Assignment Operators

Assignment operators are used to assign values to variables.

Example:

```python
x = 10
```

Here, `=` is used to assign `10` to the variable `x`.

Some assignment operators are:

- `=` → Assign a value
- `+=` → Add and assign
- `-=` → Subtract and assign
- `*=` → Multiply and assign
- `/=` → Divide and assign

Example:

```python
x = 10
x += 5

print(x)
```

Output:

```text
15
```

`x += 5` is the same as:

```python
x = x + 5
```

## 3. Comparison Operators

Comparison operators are used to compare two values.

The result is usually `True` or `False`.

Example:

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Common comparison operators:

- `==` → Equal to
- `!=` → Not equal to
- `>` → Greater than
- `<` → Less than
- `>=` → Greater than or equal to
- `<=` → Less than or equal to

## 4. Logical Operators

Logical operators are used to combine conditions.

There are three main logical operators:

- `and`
- `or`
- `not`

### `and`

Returns `True` when both conditions are `True`.

Example:

```python
age = 23

print(age > 18 and age < 30)
```

### `or`

Returns `True` when at least one condition is `True`.

Example:

```python
age = 23

print(age > 25 or age == 23)
```

### `not`

It reverses the result.

Example:

```python
age = 23

print(not age > 18)
```

## What I Learned Today

Today I learned about operators in Python. I practiced arithmetic operators, assignment operators, comparison operators and logical operators.

I also practiced these operators by creating a simple calculator program.
