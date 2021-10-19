import validdate
from  Vaccination_Request_database import Vaccination_Request_datebase
from Vaccination_Requst import  Vaccination_Request
import copy

class Options:
    def __init__(self, db_, snapshots):
        self.snapshots = snapshots
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
            self.db.database.append(new)
            self.db.file(new, "Element added ")
            self.snapshots.append(copy.deepcopy(self.db.make_snapshot()))
        except TypeError:
            print("There are not enough arguments")
            self.option1()

    def option2(self):
        self.db.del_by_ident(int(input("Enter id: ")))
        self.snapshots.append(copy.deepcopy(self.db.make_snapshot()))

    def option3(self):
        self.db.edit_elem(int(input("Enter id: ")))
        self.snapshots.append(copy.deepcopy(self.db.make_snapshot()))

    def option4(self):
        try:
            self.db.sort_date(input("Enter Attribute"))
            self.snapshots.append(copy.deepcopy(self.db.make_snapshot()))
        except AttributeError:
            print("Attribute isn't valid")
            return self.option4()

    def option5(self):
        self.db.print()

    def option6(self):
        self.db.find_all(input("Enter data"))

    def option7(self):
        file = open('out', 'w')
        file.truncate(0)
        file.close()
        exit()

    def undo(self):
        if not len(self.snapshots):
            return
        memento = self.snapshots[len(self.snapshots)-2]
        self.snapshots.pop()
        try:
            self.db.restore(memento)
        except Exception:
            self.undo()

    def redo(self):
        try:
            index = int(input("Enter index: "))
            if not len(self.snapshots) and index > 0 and index < len(self.snapshots):
                return
            memento = self.snapshots[index]
            self.snapshots.pop()
            self.db.restore(memento)
        except Exception:
            self.redo()


    def history(self):
        for i in range(len(self.snapshots)):
            print(f"Snapshot 0.{i}")
            for j in range(len(self.snapshots[i].database)):
                print(self.snapshots[i].database[j])

        #3 Igor 0123456789 0 2020-11-03 10:00 11:00