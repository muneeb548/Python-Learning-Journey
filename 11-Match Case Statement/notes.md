# Match Case Statement in Python

## What is Match Case?

The `match-case` statement is used to compare a value with different possible cases.

It is useful when we want to perform different actions based on the value of a variable.

It can be used as an alternative to multiple `if-elif-else` conditions in some situations.

## Basic Syntax

```python
match variable:
    case value1:
        # Code
    case value2:
        # Code
    case _:
        # Default case
```

## How Match Case Works

* `match` is used to specify the value we want to check.
* `case` is used to define a possible matching value.
* If a case matches the value, its code is executed.
* `case _:` works as a default case when no previous case matches.
* Only the first matching case is executed.

## Example

```python
x = int(input("Enter the Value Of X: "))

match x:

    case 0:
        print("Case is zero:")

    case 4:
        print("Case is Four:")

    case _ if x != 90:
        print(x, "is not 90:")

    case _:
        print(x)
```

## Understanding the Example

### Case 0

If the user enters `0`:

```python
case 0:
    print("Case is zero:")
```

The output will be:

```text
Case is zero:
```

### Case 4

If the user enters `4`:

```python
case 4:
    print("Case is Four:")
```

The output will be:

```text
Case is Four:
```

### Case with a Condition

```python
case _ if x != 90:
    print(x, "is not 90:")
```

Here, `_` matches any value, but the additional condition `x != 90` must also be true.

So, if the value is not `90`, this case will execute.

### Default Case

```python
case _:
    print(x)
```

The `_` is a wildcard. It works like a default case.

If no previous case matches, this case will execute.

For example, if the user enters `90`, the previous condition `x != 90` becomes false, so the final `case _:` executes.

## Match Case vs If-Elif-Else

### Using If-Elif-Else

```python
if x == 0:
    print("Case is zero")
elif x == 4:
    print("Case is Four")
else:
    print("Other value")
```

### Using Match Case

```python
match x:
    case 0:
        print("Case is zero")
    case 4:
        print("Case is Four")
    case _:
        print("Other value")
```

Both can be used to handle multiple possibilities, but `match-case` provides a clean way to match values and patterns.

## Important Points

1. `match` is used to check a value.
2. `case` defines possible matches.
3. `case _:` is used as a default or wildcard case.
4. `case _ if condition:` allows an additional condition.
5. Proper indentation is required.
6. The first matching case is executed.
7. `match-case` was introduced in **Python 3.10**.

## Summary

The `match-case` statement is a useful Python feature for matching a value against different cases. The `case _:` wildcard can be used as a default case, while `case _ if` allows us to add an extra condition.
