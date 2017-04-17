class: center, middle

# Intermediate Python

???

Notes for the _first_ slide!

---

# Purpose of this talk

- Better understanding of things you may already know (common Python internals)
- Learn how to use features you may not already know

--

### *Understand* Python

- What happens when you `import` a Python file (module)?
- What is `*args` and `**kwargs` and how do they work?
- What is the difference between the following?
    - `a = b`
    - `a == b`
    - `a is b`
- What's a mutable (vs immutable) type and why should I care?

[NOTE]: UPDATE ME WHEN FINISHED

???

A lot of the things discussed and explained in this talk can be learned by looking at the official documentation on python.org. No part of the material here is advanced or esoteric. However, many things we will discuss today are features and behaviours that are often ignored even by advanced Python users.

---

# `import`

Check out this great Python file, called `greetings.py`

```python
def greet(name):
    print("Hello, {}".format(name))

def morning_greet(name):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")
```

What happens when we run it on the terminal?

--
```
$ python greetings.py
```
--
```
$
```
(i.e., nothing)

---

# `import`

Is anyone surprised?

Let's open up **ipython** and `import it`

--

```python
In [1]: import greetings

In [2]: greetings
Out[2]: <module 'greetings' from '... greetings.py'>
```
We now have imported a module called `greetings` (which is defined in the file `greetings.py`)

--

What now?

---

# `import`

## Calling imported functions

We know greetings defines two functions, `greet()` and `morning_greet()`, both of which take a `name`.

--

```python
In [3]: name = "Alice"

In [4]: greetings.greet(name)
Hello, Alice

In [5]: greetings.morning_greet(name)
Good morning, Alice.
I hope you have a nice day.
```

---

# `import`

Why do we need to prefix function calls with `greetings.<func>`?

`greetings` is the name of the Python **module**

When you `import greetings`, Python *runs the greetings.py script* and makes all function and variable definitions under the name of the module, which by default is the name of the script file.

--
Does it really *run* the script?

