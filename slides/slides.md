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

Most of the examples I use will be boring and might even seem nonsensical: I should apologise for my lack of creativity in coming up with interesting examples.

---

class: center, middle

## The `import` statement

---

# `import`

This should look familiar

```python
[ipython]
In [1]: import numpy as np

In [2]: arr = np.array([1, 5, 2])

In [3]: np.sum(arr)
Out[3]: 8
```
or maybe
```python
[ipython]
In [1]: import os

In [2]: os.listdir(".")
Out[2]:
['index.html',
'slides.md']
```

???

For the first part of this talk, I want to explain how you can make your own little importable python files (called modules) and what happens when you execute an import.

---

# `import`

Check out this amazing Python file, called `greetings.py`

```python
[greetings.py]
def greet(name):
    print("Hello, {}".format(name))

def morning_greet(name):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")
```

What happens when we run it on the terminal?

--
```
[shell]
$ python greetings.py
$
```
(i.e., nothing)

???

Nothing happens because our script simply DEFINES some functions. It doesn't do anything with them.

---

# `import`

Is anyone surprised?

Let's open up **ipython** and `import` the file

--

```python
[ipython]
In [1]: import greetings
```
Ok so far…

--
```python
[ipython]
In [2]: greetings
Out[2]: <module 'greetings' from '... greetings.py'>
```

???

We now have a module called `greetings` which is defined in the file `greetings.py`

--

What now?

---

# `import`

## Calling imported functions

We know greetings defines two functions (we are the ones who wrote the module after all).

The two functions are called `greet()` and `morning_greet()`, both of which take a `name` argument.

--

```python
[ipython]
In [3]: name = "Alice"

In [4]: greetings.greet(name)
Hello, Alice

In [5]: greetings.morning_greet(name)
Good morning, Alice.
I hope you have a nice day.
```

---

# `import`

Why do we prefix our function calls with `greetings.<func>`?

--

`greetings` is the name of the Python **module**.

The functions `greet()` and `morning_greet()` are defined **inside** the `greetings` module.

--

When you `import greetings`:
- Python *runs the greetings.py script*
- Makes all function and variable definitions available under the name of the module
  - The module name is the name of the script file

???

When you execute import <something>, the <something> is the name of the module. Python will look for a module called <something>.py. A module can be defined in a couple of different ways, but for now, we'll look at just single file modules.

When we do `import greetings`, Python finds the file called `greetings.py`, so it imports it as the module called `greetings`.

---

# `import`

Python *runs the script* on import...

???

Notice how I said Python RUNS the greetings.py script?

That's in no way an inaccurate statement. Python literally runs the script as if it's executed.

Sort of...

--
literally

```python
[greetprint.py]
def greet(name):
    print("Hello, {}".format(name))


def morning_greet(name):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")


print("Oh my, it looks like someone just imported me ...")
```

(same as before, but has a nice little print statement at the bottom)

--

```python
[ipython]
In [1]: import greetprint
Oh my, it looks like someone just imported me ...

In [2]:
```

???

Python will in fact RUN the script, which in this case consists of TWO function definitions and a single print statement.

The reason we only get one print statement and not four is that when a def is found (a function definition), the BODY of the function is NOT executed. A def block defines a function and makes the name available so that the BODY can be executed when its CALLED.

---

# `from _ import _`

Normal `import` makes the functions available under the module name  
(e.g., `greetings.greet()`)

What if we only want one of the functions and we don't like typing `greetings.` every time?

```python
[ipython]
In [1]: from greetings import morning_greet

In [2]: morning_greet("Bob")
Good morning, Bob.
I hope you have a nice day.
```

---

# `from _ import *`

Alternatively you can just import everything


```python
[ipython]
In [1]: from greetings import *

In [2]: greet("Charlie")
Hello, Charlie

In [3]: morning_greet("Diana")
Good morning, Diana.
I hope you have a nice day.
```

--

.bad[Never do this!]

???

You should generally avoid doing this

--

.okish[Unless you really have to...]

???

However, you will find out that in Python, a lot of times when we say never do this

it's followed by "unless you really have to"

--

.good[Or a library's documentation suggests it.]

(e.g., the Brian simulator)

???

For instance, if the tutorial or documentation for a library tells you to

you might as well go ahead and do it

---

class: center, middle

## Functions

---

name: funcslide-01

# def

```python
[ipython]
In [1]: def capitalise(name):
   ...:     name = name[0].upper() + name[1:].lower()
   ...:     return name
   ...:
```

---

template: funcslide-01

What does this do?

---

template: funcslide-01

.strike[What does this do?]

What gets **executed** here?

???

Hint: Only one line is actually executed.

The body of the function is not run, only the header which **defines** the function.

---

# def

Let's define a function with an error in it

```python
[ipython]
In [1]: def broken_function():
   ...:     print("This line is fine")
   ...:     a = "string" + 10
   ...:     print("This line won't be executed.")
   ...:     print("Neither will any below it...")
   ...:     print("Adding 'str' to 'int' will cause an error")
   ...:     print("Not when it's defined, but when it's called")
   ...:

In [2]: # no error so far

In [3]: broken_function()
This line is fine
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
----> 1 broken_function()
----> 3     a = "string" + 10
TypeError: must be str, not int
```

---

# def

Same thing, but `import` it from a python file

```python
[ipython]
def broken_function():
    print("This line is fine")
    a = "string" + 10
    print("This line won't be executed.")
    print("Neither will any below it...")
    print("Adding 'str' to 'int' will cause an error")
    print("Not when it's defined, but when it's called")
```

```python
[ipython]
In [1]: import broken

In [2]: broken.broken_function()
This line is fine
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
----> 1 broken.broken_function()
----> 3     a = "string" + 10
TypeError: must be str, not int
```

---

# def

How is this information useful?

--

I'll get back to that in a minut...

--

name: default-args-01

FIRST let's look at *default argument values*

--

Remember our greeting functions?

```python
[greetings.py]
def greet(name):
    print("Hello, {}".format(name))


def morning_greet(name):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")
```

---

template: default-args-01

Now the arguments have a default value

```python
[greetdefaults.py]
def greet(name="user"):
    print("Hello, {}".format(name))


def morning_greet(name="user"):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")
```

---

name: default-args-02

# def


```python
[greetdefaults.py]
def greet(name="user"):
    print("Hello, {}".format(name))


def morning_greet(name="user"):
    print("Good morning, {}.".format(name))
    print("I hope you have a nice day.")
```

---

template: default-args-02

So now we can do this

```python
[ipython]
In [1]: import greetdefaults

In [2]: greetdefaults.greet()
Hello, user

In [3]: greetdefaults.morning_greet()
Good morning, user.
I hope you have a nice day.
```

---

template: default-args-02

Of course, the normal way still works

```python
[ipython]
In [4]: greetdefaults.greet("Elliot")
Hello, Elliot
```

---

# def

With the old definitions
