import math

class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def liitmine(self):
        return self.a + self.b
    def lahutamine(self):
        return self.a - self.b
    def korrutamine(self):
        return self.a * self.b
    def jagamine(self):
        return self.a / self.b
    def jaak(self):
        return self.a % self.b
    def ruutjuur(self):
        return math.sqrt(self.a)
    def astendamine(self):
        return self.a ** self.b
    def protsent(self):
        return self.b / self.a * 100
    def (self):
        return

a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))

kalk = cal(a,b)
while True:
    def menu():
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n7. astendamine\n8. protsent. ')
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 7:
        print("Vastus: ", kalk.astendamine())
        break
    elif valik == 8:
        print("Vastus: ", kalk.protsent())
        break
    elif valik == 0:
        print('Sisesta uuesti üks liitmise operaator')
        break




