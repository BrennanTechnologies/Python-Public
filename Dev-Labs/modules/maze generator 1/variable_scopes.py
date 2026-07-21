'''
LEGB
Local, Enclosing, Global, Built-in
'''
# Built-in
import builtins  # min, max, print, etc

# Global
x = 'global x'


def test():
    # Enclosing
    x = 'enclosing x'

    def inner():
        # Local
        x = 'local x'
        print(x)

    inner()
    print(x)


test()
print(x)
