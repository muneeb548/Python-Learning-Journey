# For Loops in Python

## What is a For Loop?

A `for` loop is used to repeat a block of code for each item in a sequence or collection.

It is commonly used to iterate over:

* Strings
* Lists
* Tuples
* Dictionaries
* Ranges
* Other iterable objects

### Basic Syntax

```python
for variable in sequence:
    # code to execute
```

The loop takes one item at a time from the sequence and stores it in the loop variable.

---

## 1. Iterating Through a String

A string is a sequence of characters, so we can use a `for` loop to access each character one by one.

### Example

```python
name = "Muneeb"

for character in name:
    print(character)
```

### Output

```text
M
u
n
e
e
b
```

Here, `character` gets one character at a time from the string.

---

## 2. Iterating Through a List

A `for` loop can be used to access each item in a list.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Mango
```

The loop runs once for each item in the list.

---

## 3. Iterating Through a Tuple

Tuples can also be iterated using a `for` loop.

### Example

```python
numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)
```

### Output

```text
10
20
30
40
```

---

## 4. Using `range()` with a For Loop

The `range()` function generates a sequence of numbers.

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

Important:

`range(5)` starts from `0` and stops before `5`.

So:

```python
range(5)
```

means:

```text
0, 1, 2, 3, 4
```

---

## 5. `range(start, stop)`

We can specify where the range should start and stop.

### Example

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

The start value is included, but the stop value is not included.

---

## 6. `range(start, stop, step)`

The third value is called the `step`.

It controls how much the number changes after every iteration.

### Example

```python
for i in range(1, 11, 2):
    print(i)
```

### Output

```text
1
3
5
7
9
```

Here:

* Start = `1`
* Stop = `11`
* Step = `2`

The loop increases the number by `2` each time.

---

## 7. Counting Backwards Using `range()`

We can use a negative step to count backwards.

### Example

```python
for i in range(10, 0, -1):
    print(i)
```

### Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

## 8. Using `for` Loop with `if`

A `for` loop can be combined with conditional statements.

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

### Output

```text
2
4
6
```

The loop checks every number, and the `if` condition prints only even numbers.

---

## 9. Using `break` in a For Loop

The `break` statement stops the loop completely.

### Example

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

### Output

```text
1
2
3
4
```

When `i` becomes `5`, `break` stops the loop.

---

## 10. Using `continue` in a For Loop

The `continue` statement skips the current iteration and moves to the next one.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
1
2
4
5
```

When `i` is `3`, that iteration is skipped.

### Difference Between `break` and `continue`

| Statement  | Purpose                     |
| ---------- | --------------------------- |
| `break`    | Stops the entire loop       |
| `continue` | Skips the current iteration |

---

## 11. Nested For Loops

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

The inner loop runs completely for each iteration of the outer loop.

Nested loops are commonly used for working with tables, patterns, and multiple collections.

---

## 12. Iterating Through a Dictionary

A `for` loop can also be used with dictionaries.

### Iterating Through Keys

```python
student = {
    "name": "Muneeb",
    "age": 23,
    "city": "Hassan Abdal"
}

for key in student:
    print(key)
```

### Output

```text
name
age
city
```

### Iterating Through Values

```python
for value in student.values():
    print(value)
```

### Output

```text
Muneeb
23
Hassan Abdal
```

### Iterating Through Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

### Output

```text
name Muneeb
age 23
city Hassan Abdal
```

---

## 13. For Loop with `else`

Python also allows an `else` block with a `for` loop.

The `else` block runs when the loop finishes normally.

### Example

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

### Output

```text
0
1
2
3
4
Loop completed
```

If the loop is stopped using `break`, the `else` block does not run.

### Example

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

The `else` block does not execute because the loop was stopped using `break`.

---

## 14. Common Use of For Loops

For loops are commonly used for:

* Processing every character in a string
* Processing every item in a list
* Working with tuples
* Generating numbers using `range()`
* Searching through data
* Filtering values using `if`
* Repeating a task a specific number of times
* Working with dictionaries
* Creating patterns using nested loops

---

## Important Points

1. A `for` loop repeats code for each item in a sequence or iterable.
2. Strings can be iterated character by character.
3. Lists and tuples can be iterated item by item.
4. `range()` is useful when we need a sequence of numbers.
5. `range(start, stop)` does not include the `stop` value.
6. `range(start, stop, step)` allows us to control the increment or decrement.
7. `break` stops the entire loop.
8. `continue` skips the current iteration.
9. A `for` loop can be combined with `if`, `elif`, and `else`.
10. A loop inside another loop is called a nested loop.
11. Dictionaries can be iterated through keys, values, or both.

---

## For Loop vs While Loop

| For Loop                                                                      | While Loop                                       |
| ----------------------------------------------------------------------------- | ------------------------------------------------ |
| Used when iterating over a sequence or when the number of iterations is known | Used when repetition depends on a condition      |
| Commonly works with strings, lists, tuples, and `range()`                     | Continues while a condition is `True`            |
| Automatically moves to the next item                                          | We usually need to update the condition manually |

### Example of For Loop

```python
for i in range(5):
    print(i)
```

### Example of While Loop

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

Both can repeat code, but they are useful in different situations.

---

## Summary

A `for` loop is one of the most commonly used loops in Python.

Basic structure:

```python
for variable in sequence:
    # code
```

It can be used with strings, lists, tuples, dictionaries, and `range()`.

The most important concepts to remember are:

```text
for       → repeat for each item
range()   → generate a sequence of numbers
break     → stop the loop
continue  → skip the current iteration
```
