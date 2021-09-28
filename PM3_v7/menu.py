from Vaccination_Request_database import Vaccination_Request_datebase
from Vaccination_Requst import Vaccination_Request

def exit_comand():
    ext = str(input("Stop program? Y/N "))
    if (ext.upper() == "Y"):
       exit()
    elif ext.upper() == "N":
        return
    else:
        return exit_comand()

def enter_int(mesg):
    try:
        n = abs(int(input(mesg)))
    except ValueError:
        print("Your velue isn't valid")
        return enter_int(mesg)
    if n > 0 and n < 5:
        return n
    else:
        enter_int("What are we going to do?\n1 - delete element\n2 - edit element\n 3 - add element")

def enter_ident():
    return input("Enter identifier:")


def menu(db):
    n = enter_int("What are we going to do?\n1 - delete element\n2 - edit element\n 3 - add element\n 4 - print database")
    if n == 1:
        db.del_by_ident(enter_ident())
    elif n == 2:
        db.edit_elem(enter_ident())
    elif n == 3:
        new = Vaccination_Request()
        db.datebase.append(new.input())
    elif n == 4:
        for i in range(len(db.datebase)):
            db.datebase[i].write()
