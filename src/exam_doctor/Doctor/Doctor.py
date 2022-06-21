class Doctor:
    def __init__(self, name, surname, scedule):
        self.name = name
        self.surname = surname
        self.scedule = scedule

    def __repr__(self):
        return f'Doctor {self.name} {self.surname} schedule {self.scedule}'