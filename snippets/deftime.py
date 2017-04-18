from time import time


def print_function_time(t=time()):
    print("This function was defined at {}".format(t))
    now = time()
    print("However, the current timestamp is {}".format(now))
