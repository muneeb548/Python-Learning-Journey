# String Slicing and Operations on Strings

Today I learned about **String Slicing and Operations on Strings** in Python.

## Length of a String

We can find the length of a string using the `len()` function.

The `len()` function returns the total number of characters in a string.

Example:

```python
fruit = "Mango"

mangolen = len(fruit)

print(mangolen)
```

Output:

```text
5
```

Here, `"Mango"` contains 5 characters, so `len(fruit)` returns `5`.

## Accessing Characters of a String

A string is a sequence of characters. Each character has an index.

The index starts from `0`.

For example:

```text
M  a  n  g  o
0  1  2  3  4
```

We can access a character using square brackets `[]`.

Example:

```python
fruit = "Mango"

print(fruit[0])
```

Output:

```text
M
```

## String Slicing

String slicing is used to access a specific part of a string.

### Syntax

```python
string[start:end]
```

The **start index is included**, but the **end index is not included**.

Example:

```python
fruit = "Mango"

print(fruit[0:4])
```

Output:

```text
Mang
```

Here:

* Index `0` is included.
* Index `4` is not included.
* Therefore, characters from index `0` to `3` are printed.

## Another Example of Slicing

```python
fruit = "Mango"

print(fruit[1:4])
```

Output:

```text
ang
```

Here, indexes `1`, `2`, and `3` are included, while index `4` is not included.

## Negative Indexing

Python also allows us to access characters using **negative indexes**.

Negative indexing starts from the end of the string.

For example:

```text
M  a  n  g  o
-5 -4 -3 -2 -1
```

Example:

```python
fruit = "Mango"

print(fruit[-3:-1])
```

Output:

```text
ng
```

Here:

* `-3` is included.
* `-1` is not included.
* Therefore, the characters at `-3` and `-2` are printed.

## What I Learned Today

Today I learned:

* How to find the length of a string using `len()`.
* How string characters are stored using indexes.
* How to access characters using square brackets `[]`.
* How to perform string slicing using `[start:end]`.
* The end index in slicing is not included.
* How to use negative indexes in string slicing.
