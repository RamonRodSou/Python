class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoas):
    def __init__(self, id_cliente, nome, idade):
        super().__init__(nome, idade)
        self.id_cliente = id_cliente

class Vendedor(Pessoas):
    def __init__(self, id_vendedor, nome, idade):
        super().__init__(nome, idade)
        self.id_vendedor = id_vendedor


c1 = Cliente('Ramon', 21, 2)

v1 = Vendedor('Antonio', 20, 1)

print(c1.id_cliente)
print(c1.idade)
print(c1.nome)

print('--------------------')

print(v1.id_vendedor)
print(v1.idade)
print(v1.nome)



# class Cliente(Pessoas):
#      def __init__(self, id):
#          self.id =id


# c1 = Cliente(2)
#  print(c1.nome)      # isso aqui nao vai funcionar, pq eu sobrepos o atributo init na classe cliente
#                       # entaot td que ela tinha na classe Pai nao vai ter mais