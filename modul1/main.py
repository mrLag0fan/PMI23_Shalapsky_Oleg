from VaccinationRequest import VaccinationRequest

db = VaccinationRequest()
db.fill_datebase()
print(db.time_max())
print(db)