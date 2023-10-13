class Animal:

    def andar (self):
        print('Estou andando como um animal')
    def correr (self):
        print ('Estou correndo como um animal')
    def pular (self):
        print ('Estou pulando como um animal')

class Felino (Animal):
    def felino (self):
        print ('Sou um felino')

class Gato (Felino):
    def miar (self):
        print ('Miando como um Gato!')

class Cachorro (Animal):
    def latir (self):
        print ("Estou Latindo como um Cachorro!")

class Passaro ():
    def voando (self):
        print ("Estou voando como um Passaro!")

class Galina (Passaro, Animal):
        def chocando (self):
            print ("Estou chocando como uma Galinha!")


g1 = Gato()
g1.pular()
g1.miar()

print('-------------')

c1 = Cachorro()
c1.correr()
c1.latir()

print('-------------')

p1 = Galina()
p1.voando()
p1.chocando()
p1.correr()

