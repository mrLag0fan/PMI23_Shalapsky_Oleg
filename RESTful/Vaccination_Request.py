import validdate

class VaccinationRequest:
    count_of_feilds = 6
    vaccines = ["pfizer", "Moderna", "AstraZeneca"]

    def __init__(self, patient_name, patient_phone, vaccine_, date_, start_time_, end_time_):
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine_
        self.date = date_
        self.start_time = start_time_
        self.end_time = end_time_

    @classmethod
    def default(cls):
        return cls("Name", "0123456789", 0, "2021-11-12", "11:00", "12:00")

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
    @validdate.check_bound(vaccines=vaccines)
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
        self.__start_time = str(start_time)

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    @validdate.check_str
    @validdate.time_valid
    @validdate.check_end_time(start_time_=start_time)
    def end_time(self, end_time):
        self.__end_time = str(end_time)
