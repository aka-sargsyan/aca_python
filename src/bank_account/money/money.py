class Money:
    EXCHANGE = {"AMD": 1, "RUB": 5, "USD": 500, "EUR": 600}

    def __init__(self, crc, val):
        self.currency = crc
        self.amount = val

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def __add__(self, other):
        x = self.amount
        if self.currency == other.currency:
            x += other.amount
        else:
            rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]
            x += (rate * other.amount)
        return Money(self.currency, x)

    def __mul__(self, n):
        return Money(self.currency, self.amount * n)




# TEST

# m1 = Money('USD', 100)
#
# #print("m1 =", m1)
#
# m2 = Money('EUR', 200)
#
# #print("m2 =", m2)
#
# #m3 = Money("RUB", 10000)
#
# m1 - m2             # m1.__add__(m2)
#
# #print("m1 + m2 = ", m3)