import operator
import validdate
from Vaccination_Requst import Vaccination_Request


class Snapshot:
    def __init__(self, database):
        self.__database = database

    @property
    def database(self):
        return self.__database

class Vaccination_Request_datebase:

    def make_snapshot(self):
        return Snapshot(self.database)

    def __init__(self):
        self.__database = []

    def __str__(self):
        for i in self.__database:
            yield str(i)

    @property
    def database(self):
        return self.__database

    def restore(self, snapshot: Snapshot):
        self.__database = snapshot.database

    def print(self):
        for i in range(len(self.database)):
            print(self.database[i])

    def file(self, vr, msg):
        print(msg)
        file_w = open("out", "a+")
        file_w.writelines(msg + str(vr))

    def fill_datebase(self):
        file = open("in", 'r')
        date = file.read()
        arr = date.split("\n")
        for n in range(len(arr)):
            arr[n] = arr[n].split(" ")
        for i in range(len(arr)):
            self.add_elem(arr[i])

    def find_by_id(self, id_):
        for item in self.database:
            if item.id == str(id_):
                return item


    def find_elem(self, id):
        item = self.find_by_id(id)
        return item

    def find_all(self, val, ratio=80):
        for i in self.database:
            fields = i.get_all_fields()
            for j in fields:
                if str(j).find(str(val)) != -1:
                    print(str(i))

    def add_elem(self, elem):
        vr = Vaccination_Request(*elem)
        self.database.append(vr)
        self.file(vr, "Element added: ")
        print(vr)

    def sort_date(self, attribute):
        self.__datebase = sorted(self.database, key=operator.attrgetter(attribute))


    def del_by_ident(self, id):#to do
        to_del = self.find_elem(id)
        self.file(to_del, "Element deleted")
        self.database.remove(to_del)

    def edit_elem(self, id):
        to_edit = self.find_elem(id)
        index = self.database.index(to_edit)
        arr = input("Enter object: ").split(" ")
        new = Vaccination_Request(*arr)
        self.database[index] = new
        self.file(to_edit, "Element edited")


