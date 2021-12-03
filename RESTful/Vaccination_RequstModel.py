from main import db
import validdate
class VaccinationRequestModel(db.Model):

    vaccines = ["pfizer", "Moderna", "AstraZeneca"]#вакцини можуть бути тільки з цих і щоб не перевіряти на правильність написання назви вакцини ми вибираємо одну з них.
                                                   #якщо прийдеться додати нову ми просто записуємо в цей масив

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    patient_phone = db.Column(db.String(10))
    vaccine = db.Column(db.Integer)
    date = db.Column(db.String(11))
    start_time = db.Column(db.String(10))
    end_time = db.Column(db.String(10))

    def __init__(self, patient_name = "Igor", patient_phone = "0123456789", vaccine_=0,
                 date_="2020-11-12", start_time_="11:00", end_time_="12:00"):
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine_
        self.date = date_
        self.start_time = start_time_
        self.end_time = end_time_
