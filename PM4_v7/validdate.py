#from Vaccination_Requst import Vaccination_Request
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
            print("The value must be a number for function {} to work".format(func.__name__))
            return func(self, int(input()))
    return func_wrapper


def check_str(func):
    def func_wrapper(self, x):
        try:
            if not isinstance(x, str):
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            print("The value must be a String for function {} to work".format(func.__name__))
            return func(self, input())
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
                print("The value must be a String for function {} to work".format(func.__name__))
                return func(self, input())
        return func_wrapper
    return decorator

def check_positive(func):
    def func_wrapper(self, x):
        if int(x) < 0:
            print("The value must be positive then 0 for function {} to work".format(func.__name__))
            return func(self, int(input()))
        res = func(self, x)
        return res
    return func_wrapper


def without_special_chars(func):
    def func_wrapper(self, x):
        symb = re.search(r'[0-9,+,${}!@#%^&*()-=_№:.;/<>\\|?]', x)
        if symb != None:
            print("The value should not contain symbol function {} to work".format(func.__name__))
            return func(self, int(input()))
        res = func(self, x)
        return res
    return func_wrapper


def check_patiant_phone(func):
    def func_wrapper(self, x):
        try:
            if len(str(x)) != 10:
                raise ValueError
            res = func(self, x)
            return res
        except ValueError:
            print(f"Patient Phone isn't valid {x}")
            return func(self, int(input("Enter Patient Phone: ")))
    return func_wrapper


def date_valid(func):
    def func_wrapper(self, x):
        try:
            date_ = datetime.strptime(x, '%Y-%m-%d').date()
            res = func(self, x)
            return res
        except ValueError:
            print(f'Data is not valid {x}')
            return func(input('Enter a date in YYYY-MM-DD format'))
    return func_wrapper

def time_valid(func):
    def func_wrapper(self, x):
        try:
            time = datetime.strptime(x, "%H:%M").time()
            res = func(self, x)
            return res
        except:
            print(f'Time is not valid {x}')
            return func(input('Enter a time in HH:MM format'))
    return func_wrapper

def check_end_time(start_time_):
    def decorator(func):
        def func_wrapper(self, x):
            if str(self.start_time) > str(x):
                print(f"End time isn't valid {x}")
                return func(self, input("Enter a end time in HH:MM format"))
            res = func(self, x)
            return res
        return func_wrapper
    return decorator
