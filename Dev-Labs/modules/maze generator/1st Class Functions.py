#

def logger(msg):
    def log_message():
        print('Log: ', msg)
    return log_message


log = logger('Hi!')

log()
