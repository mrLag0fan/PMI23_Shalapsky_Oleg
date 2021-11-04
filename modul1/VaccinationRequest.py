from VaccinationPointRequest import VaccinationPointRequest

class VaccinationRequest:
    def __init__(self, database=[]):
        self.__database = database

    def __str__(self):
        res = ""
        for i in self.__database:
            res += str(i) + '\n'
        return res

    @property
    def database(self):
        return self.__database

    def print(self):
        for i in range(len(self.database)):
            print(self.database[i])

    def find_by_time(self, time):
        for item in self.database:
            if str(item.time)[0:5] == str(time):
                return item

    def find_by_id(self, id_):
        for item in self.database:
            if item.id == str(id_):
                return item

    def find_by_name(self, name):
        for item in self.database:
            if item.name == str(name):
                return item

    def fill_datebase(self):
        file = open("in", 'r')
        date = file.read()
        arr = date.split("\n")
        for n in range(len(arr)):
            arr[n] = arr[n].split(" ")
        for i in range(len(arr)):
            self.add_elem(arr[i])
        file.close()

    def count_on_same_time(self, time, place):
        count = 0
        for item in self.database:
            if str(item.time)[0:5] == str(time) and item.point == str(place):
                count+=1
        return count

    def add_elem(self, elem):
        if self.count_on_same_time(elem[2], elem[1]) > 19:
            print("no free places")
            return
        if (self.find_by_id(elem[0])):
            print("same id")
            return
        if (self.find_by_id(elem[3])):
            print("same name")
            return
        vr = VaccinationPointRequest(*elem)
        self.database.append(vr)

    def time_max(self):
        max_time = "10:00"
        max = 0
        time = ""
        for j in range(0, 8):
            time = f"{1}{j}:00"
            count = 0
            for item in self.database:
                if str(item.time)[0:5] == str(time):
                    count += 1
            if (count > max):
                max_time = time
                max = count

        return max_time
