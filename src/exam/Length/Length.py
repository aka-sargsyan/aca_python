from Error_value.error_value import Error_value

class Length:
    dict_to_meter = {'feet': 0.3048, 'km': 1000, 'yard': 0.9144, 'mile': 1609.34, 'm': 1}

    def __init__(self, measurement, value):

        l = [key for key in self.dict_to_meter.keys()]
        try:
            if measurement not in l:
                raise Error_value(measurement)
        except Error_value as err:
            print(err.get_error_value())
        else:
            self.measurement = measurement
            self.value = value

    def __add__(self, other):
        measurement_self = self.measurement
        value_self = self.dict_to_meter[measurement_self] * self.value
        measurement_other = other.measurement
        value_other = self.dict_to_meter[measurement_other] * other.value
        self.value = (value_self + value_other) / self.dict_to_meter[measurement_self]
        print(f'adding value is {self.value} {self.measurement}')
        return Length(self.measurement, self.value)

    def __str__(self):
        if self.measurement != 'm':
            value = f'our values is {self.dict_to_meter[self.measurement] * self.value} meters'
        else:
            value = f'it is already metr, and value is {self.value}'
        return value

    def __repr__(self):
        return f'adding value is {self.value} {self.measurement}'

