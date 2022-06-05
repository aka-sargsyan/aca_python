# Programmer
class DateError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y)
            if m < 1 or m > 12:
                raise DateError("Month", m)
            if d < 1 or d > self.MONTH_DAYS[m]:
                raise DateError("Day", d)
        except DateError as err:
            print(err)
        else:
            self.__year = y
            self.__month = m
            self.__day = d

    def __str__(self):
        m = '0' + str(self.__month) if self.__month < 10 else self.__month
        d = '0' + str(self.__day) if self.__day < 10 else self.__day
        return "{}/{}/{}".format(self.__year, m, d)

    # TODO get functions for all data-members

    def add_year(self, y):
        self.__year += y

    def add_month(self, m):
        x = self.__month + m
        self.__month = x % 12 if x % 12 != 0 else 12
        # TODO : what if x == 12?
        self.add_year(x // 13)

    def add_day(self, d):
        x = self.__day + d
        while x > self.MONTH_DAYS[self.__month]:
            mont = self.__month
            days = self.MONTH_DAYS[mont]
            x -= days
            self.__day = x
            self.add_month(1)
        else:
            self.__day = x


