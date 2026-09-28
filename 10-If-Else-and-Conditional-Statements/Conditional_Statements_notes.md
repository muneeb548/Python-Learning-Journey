# If-Else and Conditional Statements in Python

Today I learned about **Conditional Statements** in Python.

Conditional statements are used to make decisions in a program based on conditions.

Python mainly provides:

* `if` statement
* `if-else` statement
* `if-elif-else` statement
* Nested `if` statements

## 1. If Statement

The `if` statement is used to execute a block of code when a condition is `True`.

### Syntax

```python
if condition:
    # code to execute
```

Example:

```python
apple_price = 200
budget = 220

if apple_price <= budget:
    print("Alexa, Add 1kg Apple to the Cart")
```

Here, the condition is `True` because the apple price is less than or equal to the budget.

---

## 2. If-Else Statement

The `if-else` statement is used when we want to execute one block of code if the condition is `True` and another block if the condition is `False`.

### Syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

Example:

```python
apple_price = 200
budget = 220

if apple_price <= budget:
    print("Alexa, Add 1kg Apple to the Cart")
else:
    print("Alexa, Do not add Apple to the Cart")
```

Since the apple price is within the budget, the `if` block is executed.

---

## 3. If-Elif-Else Statement

The `elif` statement means **else if**.

It is used when we have multiple conditions to check.

Python checks the conditions from top to bottom. When a condition is `True`, its block is executed and the remaining conditions are skipped.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

Example:

```python
num = int(input("Enter the value of num: "))

if num < 0:
    print("Number Is Negative")

elif num == 0:
    print("Number Is Zero")

elif num == 999:
    print("Number Is Special")

else:
    print("Number Is Positive")
```

Here, the program checks whether the number is:

* Negative
* Zero
* Special number `999`
* Positive

---

## 4. Nested If Statement

A **nested if statement** means using an `if` statement inside another `if` statement.

Nested `if` statements are useful when we need to check another condition after the first condition is `True`.

### Example

```python
num = 18

if num < 0:
    print("Number is Negative")

elif num > 0:

    if num >= 10:
        print("Number is Between 10-20")

    elif num <= 10:
        print("Number is Between 1-10")

else:
    print("Number is Zero")
```

Here, the second `if` statement is inside the `elif` block. This is called a **nested if statement**.

## Important Points

* `if` checks a condition.
* `else` runs when the `if` condition is `False`.
* `elif` is used to check additional conditions.
* We can use multiple `elif` statements.
* A nested `if` means an `if` statement inside another conditional statement.
* Python uses **indentation** to define the code block.

## What I Learned Today

Today I learned about **Conditional Statements** in Python.

I learned how to use:

* `if`
* `if-else`
* `if-elif-else`
* Nested `if`

I also practiced making decisions based on values and user input.
