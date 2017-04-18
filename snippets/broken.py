def broken_function():
    print("This line is fine")
    a = "string" + 10
    print("This line won't be executed.")
    print("Neither will any below it...")
    print("Adding 'str' to 'int' will cause an error")
    print("Not when it's defined, but when it's called")
