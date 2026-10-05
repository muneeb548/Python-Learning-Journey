# While Loops in Python

## What is a While Loop?

A `while` loop is used to repeatedly execute a block of code as long as a given condition is `True`.

The loop continues running until the condition becomes `False`.

### Basic Syntax

```python
while condition:
    # code to execute
```

---

## 1. Basic While Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Output

```text
1
2
3
4
5
```

The loop starts with `i = 1` and continues while `i <= 5`.

After every iteration, `i` is increased by `1`.

---

## 2. Why Do We Update the Variable?

The condition of a `while` loop must eventually become `False`.

If we forget to update the variable, the loop may continue forever.

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Here, `i += 1` changes the value of `i` after every iteration.

When `i` becomes `6`, the condition `i <= 5` becomes `False`, so the loop stops.

---

## 3. Counting Backwards

We can also use a `while` loop for reverse counting.

```python
i = 5

while i >= 1:
    print(i)
    i -= 1
```

### Output

```text
5
4
3
2
1
```

Here, `i` decreases by `1` after every iteration.

---

## 4. While Loop with If Statement

A `while` loop can be combined with conditional statements.

```python
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
```

### Output

```text
2
4
6
8
10
```

The loop checks every number from `1` to `10` and prints only the even numbers.

---

## 5. While Loop with User Input

A `while` loop can be used when we want to repeat something until the user gives a specific value.

### Example

```python
number = 1

while number != 0:
    number = int(input("Enter 0 to stop: "))
```

The loop continues until the user enters `0`.

---

## 6. Using `break` in a While Loop

The `break` statement immediately stops the loop.

### Example

```python
i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1
```

### Output

```text
1
2
3
4
5
```

When `i` becomes `5`, `break` stops the loop.

---

## 7. Using `continue` in a While Loop

The `continue` statement skips the current iteration and moves to the next iteration.

### Example

```python
i = 0

while i < 10:
    i += 1

    if i == 5:
        continue

    print(i)
```

### Output

```text
1
2
3
4
6
7
8
9
10
```

When `i` becomes `5`, that iteration is skipped.

### Important

When using `continue` in a `while` loop, make sure the loop variable is updated before `continue`.

Otherwise, the condition may never become `False`, causing an infinite loop.

---

## 8. While Loop with Else

Python allows an `else` block with a `while` loop.

The `else` block runs when the loop finishes normally because its condition becomes `False`.

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")
```

### Output

```text
1
2
3
4
5
Loop completed
```

---

## 9. While Else with `break`

If the loop is stopped using `break`, the `else` block does not execute.

### Example

```python
i = 1

while i <= 5:
    print(i)

    if i == 3:
        break

    i += 1
else:
    print("Loop completed")
```

### Output

```text
1
2
3
```

The `else` block does not run because the loop was stopped using `break`.

---

## 10. Nested While Loops

A `while` loop inside another `while` loop is called a nested while loop.

### Example

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1
```

The inner loop runs completely for each iteration of the outer loop.

Nested loops are useful for working with patterns, tables, and repeated groups of operations.

---

## 11. Infinite While Loop

If the condition of a `while` loop always remains `True`, the loop becomes an infinite loop.

### Example

```python
while True:
    print("This loop will continue")
```

This loop does not stop on its own because `True` always remains `True`.

An infinite loop can be stopped using `break` or by stopping the program manually.

### Example with `break`

```python
i = 1

while True:
    print(i)

    if i == 5:
        break

    i += 1
```

---

## 12. For Loop vs While Loop

| For Loop                                              | While Loop                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------- |
| Commonly used to iterate over a sequence              | Commonly used when repetition depends on a condition              |
| Works well with lists, strings, tuples, and `range()` | Works well when the number of repetitions is not known beforehand |
| Moves automatically to the next item                  | We usually update the loop variable ourselves                     |
| Often used when the number of iterations is known     | Often used when the stopping condition is more important          |

### For Loop Example

```python
for i in range(1, 6):
    print(i)
```

### While Loop Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Both loops can produce the same result, but they are useful in different situations.

---

## Important Points

1. A `while` loop runs as long as its condition is `True`.
2. The condition is checked before each iteration.
3. The loop variable should usually be updated inside the loop.
4. Forgetting to update the variable can create an infinite loop.
5. `break` stops the entire loop.
6. `continue` skips the current iteration.
7. A `while` loop can have an `else` block.
8. The `else` block runs when the loop finishes normally.
9. The `else` block does not run when the loop is stopped using `break`.
10. A `while` loop can contain `if`, `elif`, and `else`.
11. A `while` loop can also be nested inside another loop.

---

## Summary

A `while` loop is useful when we want to repeat code while a condition remains `True`.

Basic structure:

```python
while condition:
    # code
```

The main concepts are:

```text
while      → repeat while condition is True
break      → stop the loop
continue   → skip the current iteration
else       → runs when the loop finishes normally
```

The most important thing to remember is that the condition of a `while` loop must eventually become `False`, unless you intentionally create an infinite loop.
