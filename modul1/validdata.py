import re
from datetime import *

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

def without_special_chars(func):
    def func_wrapper(self, x):
        symb = re.search(r'[0-9,+,${}!@#%^&*()-=_№:.;/<>\\|?]', x)
        if symb != None:
            print(f'Name is not valid {x}')
            return func(self, input())
        res = func(self, x)
        return res
    return func_wrapper

def valid_time(func):
    def func_wrapper(self, x):
        try:
            time = datetime.strptime(x, "%H:%M").time()
            if str(time) > "10:00" and str(time) < "18:00":
                res = func(self, time)
                return res
            else:
                raise ValueError
        except:
            print("The value must be a String for function {} to work".format(func.__name__))
    return func_wrapper