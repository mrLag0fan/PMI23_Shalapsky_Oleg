import validdata

class VaccinationPointRequest:
    def __init__(self, id_, point_, start_time_, patient_name):
        self.id = id_
        self.point = point_
        self.time = start_time_
        self.patient_name = patient_name

    def __str__(self):
        to_print = ""
        for keys, values in vars(self).items():
            to_print += str(keys).title() + ": " + str(values) + "\n"
        return to_print

    @property
    def id(self):
        return self.__id

    @id.setter
    @validdata.check_int
    def id(self, id_):
        self.__id = id_

    @property
    def point(self):
        return self.__point

    @point.setter
    @validdata.check_str
    @validdata.without_special_chars
    def point(self, point_):
        self.__point = point_

    @property
    def time(self):
        return self.__time

    @time.setter
    @validdata.valid_time
    def time(self, time_):
        self.__time = time_

    @property
    def patient_name(self):
        return self.__patient_name

    @patient_name.setter
    @validdata.check_str
    @validdata.without_special_chars
    def patient_name(self, patient_name_):
        self.__patient_name = patient_name_