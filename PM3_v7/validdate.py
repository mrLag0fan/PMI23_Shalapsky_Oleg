from Vaccination_Requst import Vaccination_Request
import datetime


def without_special_chars(text):
    for i in range(len(text)):
        if ord(text[i]) < 65 or (ord(text[i]) < 97 and ord(text[i]) > 90) or ord(text[i]) > 122:
            return False
    return True


def id_valid(id):
    try:
        if int(id) >= 0:
            return id
        else:
            print(f"ID isn't valid {id}")
            return id_valid(input("Enter Vaccination Request ID: "))
    except ValueError:
        print(f"ID isn't valid {id}")
        return id_valid(input())


def patiant_name_valid(patiant_name):
    if type(patiant_name) == str and len(patiant_name) < 256 and without_special_chars(patiant_name):
        return True
    else:
        return False

def patiant_phone_valid(patiant_phone):
    try:
        if len(str(patiant_phone)) == 10:
            return int(patiant_phone)
        else:
            print(f"Patient Phone isn't valid {patiant_phone}")
            return patiant_phone_valid(int(input("Enter Patient Phone: ")))
    except ValueError:
        print(f"Patient Phone isn't valid {patiant_phone}")
        return patiant_phone_valid(int(input("Enter Patient Phone: ")))

def vaccine_valid(vaccine):
    try:
        if int(vaccine) < len(Vaccination_Request.vaccines) and int(vaccine) >= 0:
            return int(vaccine)
        else:
            print(f"Vaccine Type isn't valid {vaccine}")
            return vaccine_valid(input(f"Enter Vaccine type(int from 0 to {len(Vaccination_Request.vaccines)}): "))
    except ValueError:
        print(f"Vaccine Type isn't valid {vaccine}")
        return vaccine_valid(input(f"Enter Vaccine type(int from 0 to {len(Vaccination_Request.vaccines)}({Vaccination_Request.vaccines}): "))


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def date_valid(date):
    if type(date) == str and len(date) <= 10 and len(date) >= 8:
        arr = date.split('-')
        if len(arr) == 3:
            for i in range(len(arr)):
                try:
                    int(arr[i])
                except ValueError:
                    return False
        else:
            return False
        year, month, day = map(int, date.split('-'))
    else:
        return False
    if year <= datetime.date.today().year and year >= 1970 and month < 13 and month > 0 and day > 0:
        if (is_leap_year(year) and month == 2 and day < 30) or (is_leap_year(year) == False and month == 2 and day < 29):
            return True
        elif (is_leap_year(year) and month == 2 and day >= 30) or (is_leap_year(year) == False and month == 2 and day >= 29):
            return False
        if ((month % 2 == 0 and month != 2) or month == 6 or month == 7) and day >= 32:
            return False
        elif (month % 2 == 1 and month != 7) and day >=31:
            return False
        return True
    else:
        return False

def time_valid(time):
    if type(time) == str and len(time) == 5 and time.find(":") != -1:
        hh_mm = time.split(":")
    else:
        return False
    for i in range(len(hh_mm)):
        if int(hh_mm[i]) < 0 or int(hh_mm[i]) >= 60:
            return False
    return True

def datebase_invalid_elem(datebase):
    for i in range(len(datebase)):
        if type(datebase[i]) != Vaccination_Request:
            return i
    return -1
def datebase_valid(datebase):
    for i in range(len(datebase)):
        if datebase_invalid_elem(datebase) != -1:
            return False
    return True
