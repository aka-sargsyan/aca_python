class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)

    # def add_year(self, y):
    #    self.__date.add_year(y)
    #
    def add_month(self, m):
        self.__date.add_month(m)

    def add_day(self, d):
        self.__date.add_day(d)

    def add_minute(self, m):
        self.__time.add_minute(m)
        self.__date.add_day(self.__time.get_day())

    def add_second(self, s):
        self.__time.add_second(s)
        self.__date.add_day(self.__time.get_day())

    def add_hour(self, h):
        x = self.__time.get_hour() + h
        self.__time.add_hour(x % 24)
        self.__date.add_day(x // 24)


