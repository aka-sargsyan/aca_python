# class PersonError(Exception):
#
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value
from date.date_original import DateError


class Person:

    def __init__(self, first_name, last_name, age, gender):

        self.first_name = first_name
        self.last_name = last_name
        try:
            if not age.isnumeric():
                print('age')
                raise DateError('age', age)
        except DateError as err:
            print(err)
        else:
            self.age = age
        self.gender = gender

    def __str__(self):
        return f" account name {self.first_name} {self.last_name} \n " \
               f"account age {self.age} \n " \
               f"account gender {self.gender}"
