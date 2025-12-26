# Boilerplate template for decorators
# -----------------------------------
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


# Timer
# -----------------------------------
import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1. Start the timer
        value = func(*args, **kwargs)     # 2. Call the function
        end_time = time.perf_counter()    # 3. Stop the timer
        run_time = end_time - start_time  # 4. Calculate the runtime
        # 5. Print the runtime
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        r = sum([i**2 for i in range(10000)])
        return r


# results = waste_some_time(1)
# print(results)

# Slow Down
# -----------------------------------
import functools
import time


def slow_down(func):
    """Sleep 1 second before calling the function"""

    @functools.wraps(func)                    # preserve func identity
    def wrapper_slow_down(*args, **kwargs):   # accepts any arguments
        print("Sleeping...")
        time.sleep(1)
        return func(*args, **kwargs)          # call the function with the arguments
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# results = countdown(3)
# print(results)


# Register Plugins
# -----------------------------------
import random

PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


# Log
# ----------------------------------------
def log(func):
    def wrapper_log(*args, **kwargs):
        with open("log.txt", "w") as file:
            file.write(
                "Calling function with "
                + " ".join([str(a) for a in args])
                + " "
                + " ".join([str(k) + "=" + str(v) for k, v in kwargs.items()])
                + "\n"
            )
            # file.write("Calling function: " + func.__name__ + "\n" " Args: " + str(args) + " Kwargs: " + str(kwargs) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper_log


################
# Examples:
################
# @log
# def run(a, b, c=9):
# 	return a + b + c

# result = run(1,2,c=3)
# print(result)
