# Programmer
class TimeError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Time:
    __day = 0

    def __init__(self, h, m, s):
        try:
            if h < 0 or h > 23:
                raise TimeError("Hour", h)
            if m < 0 or m > 59:
                raise TimeError("Minute", m)
            if s < 0 or s > 59:
                raise TimeError("Second", s)
        except TimeError as err:
            print(err)
        else:
            self.__hour = h
            self.__minute = m
            self.__second = s
            # finally:
        #    print("Object creation process")

    def __repr__(self):
        # TODO: add 0 if any value is < 10
        h = '0' + str(self.__hour) if self.__hour < 10 else self.__hour
        m = '0' + str(self.__minute) if self.__minute < 10 else self.__minute
        s = '0' + str(self.__second) if self.__second < 10 else self.__second
        return "{}:{}:{}".format(h, m, s)

    def get_second(self):
        return self.__second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_day(self):
        return self.__day

    def set_hour(self, x):
        if 0 < x < 23:
            self.__hour = x
            print('Value successfully changed')
        else:
            print("Sorry: Invalid value")

    def add_hour(self, h):
        # TODO: check param type
        self.__hour = (self.__hour + h) % 24
        self.__day = (self.__hour + h) // 24

    def add_minute(self, m):
        x = self.__minute + m
        self.__minute = x % 60
        self.add_hour(x // 60)

    def add_second(self, s):
        x = self.__second + s
        self.__second = x % 60
        self.add_minute(x // 60)
