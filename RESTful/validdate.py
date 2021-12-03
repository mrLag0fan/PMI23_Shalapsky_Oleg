#from Vaccination_Requst import Vaccination_Request
import copy
from datetime import datetime
import re


def check_int(func):
    def func_wrapper(self, x):
        try:
            if not isinstance(int(x), int):
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            raise ValueError("The value must be a number for function {} to work".format(func.__name__))
    return func_wrapper


def check_str(func):
    def func_wrapper(self, x):
        try:
            if not isinstance(x, str):
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            raise ValueError("The value must be a String for function {} to work".format(func.__name__))
    return func_wrapper


def check_len(length):
    def decorator(func):
        def func_wrapper(self, x):
            try:
                if len(x) >= length:
                    raise ValueError
                res = func(self, x)
                return res
            except ValueError:
                raise  ValueError("The value must be a String for function {} to work".format(func.__name__))
        return func_wrapper
    return decorator

def check_positive(func):
    def func_wrapper(self, x):
        try:
            if int(x) < 0:
                print(int(x))
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            raise ValueError(f'Id is not valid {x}')
    return func_wrapper


def without_special_chars(func):
    def func_wrapper(self, x):
        symb = re.search(r'[0-9,+,${}!@#%^&*()-=_№:.;/<>\\|?]', x)
        if symb != None:
            raise ValueError(f'Name is not valid {x}')
        return func(self, x)
    return func_wrapper


def check_patiant_phone(func):
    def func_wrapper(self, x):
        try:
            if len(str(x)) != 10:
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            raise ValueError(f"Patient Phone isn't valid {x}")
    return func_wrapper


def date_valid(func):
    def func_wrapper(self, x):
        try:
            date_ = datetime.strptime(x, '%Y-%m-%d').date()
            res = func(self, x)
            return res
        except ValueError:
            raise ValueError(f'Data is not valid {x}')
    return func_wrapper

def time_valid(func):
    def func_wrapper(self, x):
        try:
            time = datetime.strptime(x, "%H:%M").time()
            res = func(self, time)
            return res
        except ValueError:
            raise ValueError(f'Time is not valid {x}')
    return func_wrapper

def check_end_time(start_time_):
    def decorator(func):
        def func_wrapper(self, x):
            if str(self.start_time) > str(x):
                raise ValueError(f"End time isn't valid {x}")
            res = func(self, x)
            return res
        return func_wrapper
    return decorator

def check_bound(vaccines):
    def decorator(func):
        def func_wrapper(self, x):
            if x > len(vaccines):
                raise ValueError(f"End time isn't valid {x}")
            res = func(self, x)
            return res
        return func_wrapper
    return decorator