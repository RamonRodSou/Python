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

    def andar (self):
        super().andar()  # to referenciando a classe Pai
        print('Nao estou andando')      

c1 = Cliente('Ramon', 30, 123123123)
c1.andar()


#super()  referencia classe Pai acessando tudo que tem na classe
#self     referencia a instancia
#cls      a classe
