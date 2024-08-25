import functools

from utils import authenticate, is_valid_password


def authenticate_class(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if authenticate(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception('Unauthorized User')
    return wrapper


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pwd = args[0].password
        if is_valid_password(pwd):
            return func(*args, **kwargs)
        else:
            raise Exception('Invalid Password')
    return wrapper
