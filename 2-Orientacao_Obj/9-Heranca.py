class Pessoas: 
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def falar (self):
        print('Estou Falando')

    def andar (self):
        print('Estou Andando')      

   

class Vendedor(Pessoas):

    def vender (self):
        print('Estou Vendendo')     


class Cliente(Pessoas):

    def comprar (self):
        print('Estou Comprar')     

v1 = Vendedor('Ramon', 30, 123123123)
v1.andar()
v1.falar()
v1.vender()