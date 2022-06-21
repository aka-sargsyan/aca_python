class Patient:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f'{self.name} {self.surname} - {self.gender}, {self.age} years old.'