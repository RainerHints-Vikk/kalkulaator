import math #impordib math library

class cal(): #loob classi nimega cal
    def __init__(self,a,b): #loob muutujad a ja b
        self.a = a #nimetab a nimeks self.a
        self.b = b #nimetab b nimeks self.b

    def liitmine(self):    #See blokk määrab funktsioonid näiteks muutujate liitmine ja lahutamine.
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
    def protsendi_liitmine(self):
        return self.a + (self.b * self.a / 100)

a = int(input("Sisesta esimene number: "))  #küsib kasutajalt muutujat a
b = int(input("Sisesta teine number: "))   #küsib kasutajalt muutujat b

kalk = cal(a,b)  #annab cal() klassile ja sinna sisse kuuluvatele muutujatele a jab nime kalk
while True:  #skript toimib kuni tuleb break käsk
    def menu(): #defineerib menüü
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n7. astendamine\n8. protsendi leidmine\n9. protsendi liitmine') #annab nime x sulgusedes olevale textile
        print(x) #prindib texti mis on x nimetusega tähistatud
    menu()
    valik = int(input('Sisesta üks valikutest: ')) #küsib kasutajalt millist funktsiooni kasutatakse
    if valik == 1:                           #järgmised read käivitavad vastavalt valitud funktsioonile üleval tehtud classi funktsiooni.
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
    elif valik == 9:
        print("Vastus: ", kalk.protsendi_liitmine())
        break
    else: #kui sisestati number mis ei ole listis siis prinditakse all määratud tekst
        print('Sisesta uuesti üks liitmise operaator')
        break




