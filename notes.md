# Notes for Python talk at CING

Date: 29 Aug 2019

----

## Concepts

- Types, names, variables, objects.
    - Object identity and equality.
    - Mutability
    - Immutable types
    - Immutable containers which contain mutable objects.
- Namespaces.
    - Local scopes, global and nonlocal keywords.
- Classes.
    - Static methods, class methods.  Constructor, magic methods.


https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects
"A special quirk of Python is that – if no global statement is in effect – assignments to names always go into the innermost scope."

"Assignments do not copy data — they just bind names to objects."


## Part 0

*General Python facts and why we care*


## Part 1

The basics.


### Definitions

Let's talk about **objects**.  All data in Python is represented by **objects**.  Every object has an **identity**, a **type**, and a **value**.  **Objects** are (often) identified by a symbolic **name**.

```python
x = 10
```

Name:             `x`
Object value:     `10`
Object type:      `int` (integer)

```python
greeting = "Hello there"
```

Name:             `greeting`
Object value:     `"Hello there"`
Object type:      `str` (string)

```python
days = ["Saturday", "Sunday"]
```

Name:             `days`
Object value:     `["Saturday", "Sunday"]`
Object type:      `list`


### (Im)mutability

Immutable types: `int`, `float`, `str`, `tuple`

Mutable types: `list`, `dict`


### Immutable objects

```python
greeting = "Hello"
len(greeting)
print(greeting[1])
greeting[1] = "a"  # error
```

Can't change the string since it's immutable.


```python
greeting = "Hallo"
```

Here, we're not changing the string, we're just binding (assigning) a new value (a different object) to the name `greeting`.  `greeting` refers to a different object now.


```python
greeting += " there"
print(greeting)
greeting += ", old friend"
print(greeting)
```

These are convenient ways to change the value of a **name** that has type `str`.  The latter operation `+=` is more appropriate for numerical types.

```python
x = 10
x += 3
print(x)
```


What does it mean to be **immutable** then?


### The `id()`entity of an object

```python
greeting = "hello"
print(id(greeting))

greeting.append(" there")
print(id(greeting))
```

```python
x = 10
print(id(x))
x += 20
print(id(x))
```

The immutable object's **value** doesn't change, the names `greeting` and `x` are bound to different objects (they have a new `id`).


### Mutable objects

```python
days = ["Saturday", "Sunday"]
print(id(days))
days.append("Wednesday")
print(id(days))

days += ["Thursday", "Friday"]
print(id(days))
```

The name `days` is not rebound, it's still pointing to the same object.
The object's **value** has changed.  Lists are immutable.


### What this means in practice

In practice, you should always be aware of what you are doing to an object that is or is not mutable.

```python
weekend = ["Saturday", "Sunday"]
days = weekend
print(days)
days.append("Monday")
days.append("Tuesday")
days.append("Wednesday")
print(days)
print(weekend)
print(id(days), id(weekend))
```

When we assigned `weekend` to `days`, the existing object in `weekend` we *bound* to `days`.  Both `days` and `weekend` refer to the same object (they have the same `id`).  When we modified `days` we were modifying the underlying object that is bound to both names.

### Testing identities

```python
a = ["Green", "Yellow"]
b = ["Green", "Yellow"]
print(a == b)
print(a is b)

a.append("Red")
print(a)
print(b)

a = b
print(a is b)
```
