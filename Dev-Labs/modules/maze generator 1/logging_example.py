import logging
# logging levels:
# DEGUG, INFO, WARNING, ERROR, CRITICAL
# 10, 20, 30, 40, 50 # logging levels are integers so you can compare them to each other to determine which is higher or lower than the other one (e.g. DEBUG < INFO)
#
# https://docs.python.org/3/library/logging.html#logging-levels

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)

# logging.basicConfig(filename='log_example.txt', level=logging.DEBUG)
# logging.basicConfig(filename='log_example.txt', level=logging.INFO)
# logging.basicConfig(filename='log_example.txt', level=logging.WARNING)
# logging.basicConfig(filename='log_example.txt', level=logging.ERROR)
# logging.basicConfig(filename='log_example.txt', level=logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log', filemode='w')
# logging.basicConfig(filename='example.log', level=logging.DEBUG)


def add(x, y):
    logging.debug('Add: {} + {} = {}'.format(x, y, x + y))
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error('Divide by zero error!!!!')
    else:
        return result


'''
def divideCB(x, y):
    if y == 0:
        logging.error('Divide by zero error!')
        return 'ERROR: Divide by zero error!'
    return x / y
'''


# def __init__():

num1 = 10
num2 = 0

'''
print('Add: {} + {} = {}'.format(num1, num2, add(num1, num2)))
print('Subtract: {} - {} = {}'.format(num1, num2, subtract(num1, num2)))
print('Multiply: {} * {} = {}'.format(num1, num2, multiply(num1, num2)))
print('Divide: {} / {} = {}'.format(num1, num2, divide(num1, num2)))
'''

logging.debug('Add: {} + {} = {}'.format(num1, num2, add(num1, num2)))
logging.info('Subtract: {} - {} = {}'.format(num1,
                                             num2, subtract(num1, num2)))
logging.warning('Multiply: {} * {} = {}'.format(num1,
                                                num2, multiply(num1, num2)))
logging.error('Divide: {} / {} = {}'.format(num1,
                                            num2, divide(num1, num2)))
