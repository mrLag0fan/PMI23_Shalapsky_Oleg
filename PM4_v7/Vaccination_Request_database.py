import operator
import validdate
from Vaccination_Requst import Vaccination_Request

class Vaccination_Request_datebase:

    def __init__(self):
        self.__datebase = []

    @property
    def datebase(self):
        return self.__datebase

    def print(self):
        for i in range(len(self.datebase)):
            print(self.datebase[i])

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

    def find_by_ID(self, id_):
        for item in self.datebase:
            if item.id == str(id_):
                return item


    def find_elem(self, id):
        item = self.find_by_ID(id)
        return item

    def add_elem(self, elem):
        vr = Vaccination_Request(*elem)
        self.datebase.append(vr)
        self.file(vr, "Element added: ")
        print(vr)

    def sort_date(self, attribute):
        self.__datebase = sorted(self.datebase, key=operator.attrgetter(attribute))


    def del_by_ident(self, id):#to do
        to_del = self.find_elem(id)
        self.file(to_del, "Element deleted")
        self.datebase.remove(to_del)

    def edit_elem(self, id):
        to_edit = self.find_elem(id)
        index = self.datebase.index(to_edit)
        arr = input("Enter object: ").split(" ")
        new = Vaccination_Request(*arr)
        self.datebase[index] = new
        self.file(to_edit, "Element edited")


