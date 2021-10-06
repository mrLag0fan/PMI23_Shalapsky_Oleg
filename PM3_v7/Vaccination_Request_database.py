import validdate
from Vaccination_Requst import Vaccination_Request
class Vaccination_Request_datebase:

    def __init__(self, datebase_ = []):
        self.datebase = datebase_

    @property
    def datebase(self):
        return self.__datebase

    @datebase.setter
    def datebase(self, datebase_):
        if validdate.datebase_valid(datebase_):
            self.__datebase = datebase_
        else:
            print("Datebase isn't valid")
            i = validdate.datebase_invalid_elem(datebase_)
            datebase_[i] = Vaccination_Request.input(datebase_[i])
            self.datebase = datebase_

    def print(self):
        for i in range(len(self.datebase)):
            self.datebase[i].write()

    def input(self):
        for i in range(len(self.datebase)):
            self.datebase.input()

    def fill_datebase(self):
        file = open("in", 'r')
        date = file.read()
        arr = date.split("\n")
        for n in range(len(arr)):
            arr[n] = arr[n].split(" ")
        for i in range(len(arr)):
            self.add_elem(arr[i])

    def add_elem(self, elem):
        vr = Vaccination_Request(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6])
        self.datebase.append(vr)#над цим ще думаю як спростит
        print("Element added")
        file_w = open("out", "a+")
        file_w.writelines("Element added: " + str(vr.to_arr()))

    def find_elem(self, date):
        str_date = str(date)
        res = []
        for i in range(len(self.datebase)):
            if str(self.datebase[i].id).find(str_date) != -1 \
                    or str(self.datebase[i].patient_name).find(str_date) != -1 \
                    or str(self.datebase[i].patient_phone).find(str_date) != -1 \
                    or str(self.datebase[i].vaccine).find(str_date) != -1 \
                    or str(self.datebase[i].date).find(str_date) != -1\
                    or str(self.datebase[i].start_time).find(str_date) != -1 \
                    or str(self.datebase[i].end_time).find(str_date) != -1:
                #self.datebase[i].print()
                res.append(self.datebase[i])
        return res

    def sort_date(self, type):
        if type == "id":
            self.datebase.sort(key=lambda x: x.id)
        elif type == "patient_name":
            self.datebase.sort(key=lambda x: x.patient_name)
        elif type == "patient_phone":
            self.datebase.sort(key=lambda x: str(x.patient_phone))
        elif type == "vaccine":
            self.datebase.sort(key=lambda x: x.vaccine)
        elif type == "date":
            self.datebase.sort(key=lambda x: str(x.date))
        elif type == "start_time":
            self.datebase.sort(key=lambda x: str(x.start_time))
        elif type == "end_time":
            self.datebase.sort(key=lambda x: str(x.end_time))
        else:
            print("Sort type isn't valid")
            return self.sort_date(input("Enter Sort Type: id/patient_name/patient_phone/vaccine/date/start_time/end_time"))

    def del_by_ident(self, ident):
        to_del = self.find_elem(str(ident))
        for i in range(len(to_del)):
            for j in range(len(self.datebase)-1):
                if to_del[i] == self.datebase[j]:
                    file = open("out", "a+")
                    print("Element deleted")
                    file.writelines("Element deleted: " + str(self.datebase[j].to_arr()))
                    del self.datebase[j]

    def edit_elem(self, ident):
        to_edit = self.find_elem(str(ident))
        for i in range(len(to_edit)):
            for j in range(len(self.datebase)):
                if to_edit[i] == self.datebase[j]:
                    self.datebase[j].input()
                    file = open("out", "w")
                    print("Element edited")
                    file.writelines("Element edited: " + str(self.datebase[j].to_arr()))


