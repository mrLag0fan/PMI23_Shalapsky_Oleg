from main import ma

class VaccinationRequestShema(ma.Schema):
    class Meta:
        fields = ('id', 'patient_name', 'patient_phone', 'vaccine', 'date', 'start_time', 'end_time')
