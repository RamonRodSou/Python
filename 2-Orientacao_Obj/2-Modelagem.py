class Pessoa:                               # Nome
    def __init__(self, nome, idade, cpf):   # Atributo
        self.nome = nome
        self.cpf = idade
        self.cpf = cpf
    def logar_sitema(self):                     #Método
        print(f'{self.nome} está logando no sistema')

p1 = Pessoa('Ramon', 30,'00022233323')
p2 = Pessoa('Samara', 31,'11122233323')

print(f'{p1.nome} é casado com {p2.nome}')

p1.logar_sitema()
p2.logar_sitema()
