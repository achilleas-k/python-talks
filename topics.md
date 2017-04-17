# Intermediate Python Features

## Description

Come level up your Python skills!

In this session, we will teach you the little things (and maybe some big things) that will increase your productivity when coding with Python.
Are you a new Python user that wants to learn what nice tricks the language has to offer?
Perhaps you're a Python user that just wants to better understand what the language is doing for you and what more it can offer.
Or maybe you're a programmer skilled in other languages that wants to learn why some of us love Python.

Join us and we will do our best to teach you:
- **The Python features that will make your life easier**  
  Do you know how to write your own modules? What are optional arguments? Have you ever heard of `*args` and `**kwargs`?
- **How Python works**  
  What happens when you put `import` at the top of your Python script? What's the difference between `==` and `is`? What's a *mutable* type?
- **How to be a better programmer and avoid common pitfalls**  
  Some of Python's best features have unexpected side effects, even for seasoned programmers. We'll help you avoid them.

Stack Overflow questions for 'gotchas':
- [Python 2.x gotcha's and landmines][so-pitfalls-1]
- [Common pitfalls in Python][so-pitfalls-2] (duplicate question, but some new answers)


## Topics

- import
- Function input/output: args, kwargs, tuple unpacking (multiple return), optional/named args

- Iteration (itertools, etc)
- Mutability (id, pass-by-ref, etc)


## Prioritised topic list (Y/M/N)

### Yes

- `*args` and `**kwargs`
- Ternary Operators
- Global & Return
- Mutation
- Enumerate, Zip, Itertools
- Object introspection
- Comprehensions

### Maybe

- Generators
- Map, Filter, Reduce
- `set` data structure
- Decorators
- Collections
- Exceptions
- Lambdas
- For-Else
- `open` function

### No

- Debugging
- `__slots__` Magic
- Virtual Environment
- One-Liners
- Python C extensions
- Coroutines
- Function caching
- Targeting Python 2+3
- Context managers


### Full topic list

*Copied from the TOC of the [Python Tips][python-tips-book] book*

This is the list of topics in the Intermediate Python Python Tips book.
The topics below were used to select the list of topics above.

1. `*args` and `**kwargs`
    - Usage of `*args`
    - Usage of `**kwargs`
    - Using `*args` and `**kwargs` to call a function
    - When to use them?
2. Debugging
3. Generators
    - Iterable
    - Iterator
    - Iteration
    - Generators
4. Map, Filter and Reduce
    - Map
    - Filter
    - Reduce
5. `set` Data Structure
6. Ternary Operators
7. Decorators
    - Everything in Python is an object:
    - Defining functions within functions:
    - Returning functions from within functions:
    - Giving a function as an argument to another function:
    - Writing your first decorator:
    - Decorators with Arguments
8. Global & Return
    - Multiple return values
9. Mutation
10. `__slots__` Magic
11. Virtual Environment
12. Collections
    - `defaultdict`
    - `OrderedDict`
    - `counter`
    - `deque`
    - `namedtuple`
    - `enum.Enum` (Python 3.4+)
13. Enumerate
14. Object introspection
    - `dir`
    - `type` and `id`
    - `inspect` module
15. Comprehensions
    - `list` comprehensions
    - `dict` comprehensions
    - `set` comprehensions
16. Exceptions
    - Handling multiple exceptions:
17. Lambdas
18. One-Liners
19. For - Else
    - `else` clause:
20. Python C extensions
    - CTypes
    - SWIG
    - Python/C API
21. `open` Function
22. Targeting Python 2+3
23. Coroutines
24. Function caching
    - Python 3.2+
    - Python 2+
25. Context managers
    - Implementing Context Manager as a Class:
    - Handling exceptions
    - Implementing a Context Manager as a Generator

[python-tips-book]: http://book.pythontips.com/en/latest/
[so-pitfalls-1]: https://stackoverflow.com/questions/530530/python-2-x-gotchas-and-landmines
[so-pitfalls-2]: https://stackoverflow.com/questions/1011431/common-pitfalls-in-python?noredirect=1&lq=1
