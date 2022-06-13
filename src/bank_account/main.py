from date.time_original import Time
from money.money import Money
from date.date_original import Date
from person.person import Person

if __name__ == '__main__':
    t = Time(5, 2, 12)
    print(t)
    # p = Person('Artak', 'Sargsyan', 'bb', 'male')
    m = Money('AMD', 1000)
    m1 = Money('USD', 1000)
    d = Date(-2000, 10, 20)


    print(m + m1)
    print(d)
    # print(p)