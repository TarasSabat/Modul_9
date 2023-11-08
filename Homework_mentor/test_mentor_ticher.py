def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner
​
@error_handler
def add(*args, **kwargs):
    name, phone = args
    user[name] = phone
​
def exit_handler():
    return
​
def hello_handler():
    return 'Hello, how I can help you?'