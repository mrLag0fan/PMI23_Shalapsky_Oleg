import validdate


class Vaccination_Request:

    vaccines = ["pfizer", "Moderna", "AstraZeneca"]#вакцини можуть бути тільки з цих і щоб не перевіряти на правильність написання назви вакцини ми вибираємо одну з них.
                                                   #якщо прийдеться додати нову ми просто записуємо в цей масив

    def __init__(self, id_, patient_name, patient_phone, vaccine_,
                 date_, start_time_, end_time_):
        self.id = id_
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine_
        self.date = date_
        self.start_time = start_time_
        self.end_time = end_time_


    def __str__(self):
        to_print = ""
        for keys, values in vars(self).items():
            to_print += str(keys).title() + ": " + str(values) + "\n"
        return to_print

    @property
    def id(self):
        return self.__id

    @id.setter
    @validdate.check_int
    @validdate.check_positive
    def id(self, id_):
        self.__id = id_

    @property
    def patient_name(self):
        return self.__patient_name

    @patient_name.setter
    @validdate.check_str
    @validdate.check_len(length=255)
    @validdate.without_special_chars
    def patient_name(self, patient_name):
        self.__patient_name = patient_name


    @property
    def patient_phone(self):
        return self.__patient_phone

    @patient_phone.setter
    @validdate.check_int
    @validdate.check_positive
    @validdate.check_patiant_phone
    def patient_phone(self, patient_phone):
        self.__patient_phone = patient_phone

    @property
    def vaccine(self):
        return self.__vaccine

    @vaccine.setter
    @validdate.check_int
    @validdate.check_positive
    def vaccine(self, vaccine):
        self.__vaccine = vaccine

    @property
    def date(self):
        return self.__date

    @date.setter
    @validdate.check_str
    @validdate.date_valid
    def date(self, date):
        self.__date = date

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    @validdate.check_str
    @validdate.time_valid
    def start_time(self, start_time):
            self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    @validdate.check_str
    @validdate.time_valid
    @validdate.check_end_time(start_time_=start_time)
    def end_time(self, end_time):
        self.__end_time = end_time

    def get_all_fields(self):
        return [x for x in vars(self).values()]


#3 Igor 9876543210 2 2021-06-4 00:23 00:40