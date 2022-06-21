from Patient.Patient import Patient
from Doctor.Doctor import Doctor
from Register.Register import Register

if __name__ == '__main__':
    p1 = Patient('Artak', 'Sargsyan', 35, 'm')
    p2 = Patient('Artak2', 'Sargsyan2', 35, 'm')
    doc = {'12.06.2022': p1}
    d = Doctor('Armewn', 'kazaryan', doc)
    r = Register('Armewn', 'kazaryan', doc, '13.06.2022', p2)
    r.add_scedule()
    print(r.scedule)
    print(d)
    print(p1)

