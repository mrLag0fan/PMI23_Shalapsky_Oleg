import validdate
from  Vaccination_Request_database import Vaccination_Request_datebase
from Vaccination_Requst import  Vaccination_Request

class Options:
    def __init__(self, db_):
        self.db = db_

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db_):
        self.__db = db_

    def option1(self):
        arr = input("Enter object: ").split(" ")
        try:
            new = Vaccination_Request(*arr)
            self.db.datebase.append(new)
            self.db.file(new, "Element added ")
        except TypeError:
            print("There are not enough arguments")
            self.option1()

    def option2(self):
        self.db.del_by_ident(validdate.enter_int("Enter id: "))

    def option3(self):
        self.db.edit_elem(validdate.enter_int("Enter id: "))

    def option4(self):
        try:
            self.db.sort_date(input("Enter Attribute"))
        except AttributeError:
            print("Attribute isn't valid")
            return self.option4()

    def option5(self):
        self.db.print()

    def option6(self):
        file = open('out', 'w')
        file.truncate(0)
        file.close()
        exit()


        #3 Igor 0123456789 0 2020-11-03 10:00 11:00