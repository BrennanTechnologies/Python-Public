# Formatted string example

def foo(x):
    y = 2

    print("This is foo. " + str(x+y))

    formatted = f"This is foo. {x+y}"
    print(formatted)

    print(f"This is foo. {x+y}")

    print("This is foo. {}".format(x+y))


def bar():
    print("This is bar.")


def parodied():
    print("This function has been parodied.")


# Example usage
x = 1
foo(x)
bar()
parodied()
