class UnknownAtom(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'ther are no {self.value} atom in list'


class Atom:
    a = 'CHNOP'

    def __int__(self, name):
        try:
            for item in name:
                if item not in self.a:
                    raise UnknownAtom(item)
        except UnknownAtom as err:
            print(err)

        else:
            self.name = name

    def __str__(self):
        return 'hello'
