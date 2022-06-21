from Length.Length import Length

if __name__ == '__main__':
    l1 = Length('km', 1)
    l2 = Length('m', 2000)
    l = l1 + l2
    print(l)
    print(l.__repr__())
