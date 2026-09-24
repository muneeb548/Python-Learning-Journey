# 09 - Strings in Python

Today I learned about **Strings** in Python.

## What is a String?

In Python, anything that is enclosed between **single quotes (`' '`)** or **double quotes (`" "`)** is considered a string.

A string is a sequence of characters and is used to store textual data.

Example:

```python
name = "Raja"

print("Hello", name)
```

Output:

```text
Hello Raja
```

## Single and Double Quotes

It does not matter whether we enclose a string in single quotes or double quotes. The output remains the same.

Example:

```python
name1 = "Raja"
name2 = 'Raja'

print(name1)
print(name2)
```

Both will give the same output:

```text
Raja
Raja
```

## Using Quotation Marks Inside a String

Sometimes, we need to use quotation marks inside a string.

For example:

**He said "I want to eat an apple".**

We can use single quotes outside the string and double quotes inside it.

Example:

```python
sentence = 'He said "I want to eat an apple".'

print(sentence)
```

We can also use double quotes outside and single quotes inside:

```python
sentence = "He said 'I want to eat an apple'."

print(sentence)
```

## Multiline Strings

Python allows us to create strings that contain multiple lines.

We can use **triple single quotes (`''' '''`)** or **triple double quotes (`""" """`)** for multiline strings.

Example:

```python
message = '''Hi Raja,
How are you?
I hope you are doing well.'''

print(message)
```

Output:

```text
Hi Raja,
How are you?
I hope you are doing well.
```

## Accessing Characters of a String

In Python, a string is a sequence of characters.

Each character has an **index**.

The index starts from **0**.

We can use square brackets `[]` to access a character from a string.

Example:

```python
name = "Raja"

print(name[0])
print(name[1])
```

Output:

```text
R
a
```

Here:

* `name[0]` → `R`
* `name[1]` → `a`
* `name[2]` → `j`
* `name[3]` → `a`

## Looping Through a String

We can use a `for` loop to go through a string character by character.

Example:

```python
name = "Raja"

for character in name:
    print(character)
```

Output:

```text
R
a
j
a
```

Here, the `for` loop prints all the characters of the string one by one.

## What I Learned Today

Today I learned about **Strings** in Python.

I learned how to:

* Create strings using single and double quotes.
* Use quotation marks inside a string.
* Create multiline strings.
* Access characters using indexes.
* Understand that string indexing starts from `0`.
* Loop through a string using a `for` loop.
