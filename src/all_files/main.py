from date.time_original import Time
from money.money import Money

if __name__ == '__main__':
    t = Time(5, 2, 12)
    print(t)

    m = Money('AMD', 1000)
    m1 = Money('USD', 1000)

    print(m + m1)
