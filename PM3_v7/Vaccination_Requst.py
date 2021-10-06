from datetime import datetime
import validdate


class Vaccination_Request:

    vaccines = ["pfizer", "Moderna", "AstraZeneca"]#вакцини можуть бути тільки з цих і щоб не перевіряти на правильність написання назви вакцини ми вибираємо одну з них.
                                                   #якщо прийдеться додати нову ми просто записуємо в цей масив

    def __init__(self, id_=4, patient_name="Name", patient_phone=1234567890, vaccine_=1,
                 date_=str(datetime.today().date()), start_time_="12:50", end_time_="13:10"):
        self.id = id_
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine_
        self.date = date_
        self.start_time = start_time_
        self.end_time = end_time_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = validdate.id_valid(id_)

    @property
    def patient_name(self):
        return self.__patient_name

    @patient_name.setter
    def patient_name(self, patient_name):
        if validdate.patiant_name_valid(patient_name):
            self.__patient_name = patient_name
        else:
            print(f"Patient Name isn't valid {patient_name}")
            self.patient_name = (input("Enter Patient Name: "))

    @property
    def patient_phone(self):
        return self.__patient_phone

    @patient_phone.setter
    def patient_phone(self, patient_phone):
        self.__patient_phone = validdate.patiant_phone_valid(patient_phone)

    @property
    def vaccine(self):
        return self.__vaccine

    @vaccine.setter
    def vaccine(self, vaccine):
        self.__vaccine = Vaccination_Request.vaccines[validdate.vaccine_valid(vaccine)]

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if validdate.date_valid(date):
            self.__date = date
        else:
            print(f"Date isn't valid {date}")
            self.date = (input("Enter a date in YYYY-MM-DD format"))

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        if validdate.time_valid(start_time):
            self.__start_time = start_time
        else:
            print(f"Start time isn't valid {start_time}")
            self.start_time = (input("Enter a date in HH:MM format"))

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        if validdate.time_valid(end_time) and self.start_time < end_time:
            self.__end_time = end_time
        else:
            print(f"Start time isn't valid {end_time}")
            self.start_time = (input("Enter a date in HH:MM format"))


    def input(self):
        self.id = (input("Enter Vaccination Request ID: "))
        self.patient_name = (input("Enter Patient Name: "))
        self.patient_phone = (input("Enter Patient Phone: "))
        self.vaccine = (input(f"Enter Vaccine type(int from 0 to {len(Vaccination_Request.vaccines)}({Vaccination_Request.vaccines}): "))
        self.date = (input('Enter a date in YYYY-MM-DD format'))
        self.start_time = input("Enter a time in HH:MM format")
        self.end_time = (input("Enter a time in HH:MM format"))

    def write(self):
        print(self.id, end=' ')
        print(self.patient_name, end=' ')
        print(self.patient_phone, end=' ')
        print(self.vaccine, end=' ')
        print(self.date, end=' ')
        print(self.start_time, end=' ')
        print(self.end_time, end='\n')

    def to_arr(self):
        res = str(self.id) + " " + str(self.patient_name) + " " + str(self.patient_phone) + " " + str(self.vaccine) + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time) + '\n'
        print(res)
        return res

