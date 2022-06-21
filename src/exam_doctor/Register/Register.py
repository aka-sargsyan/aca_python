from Doctor.Doctor import Doctor
class Register(Doctor):
    def __init__(self, name, surname, scedule, patient, datetime):
        super().__init__(name, surname, scedule)
        self.patient = patient
        self.datetime = datetime

    def add_scedule(self):
        self.scedule[self.datetime] = self.patient
