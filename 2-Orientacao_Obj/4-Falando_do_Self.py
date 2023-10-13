class Pessoas:
    def __init__(self, nome, id):
        self.nome = nome   
        self.id = id

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logando no sistema')


p1 = Pessoas('Samara Rodrigues', 31)

p1.logar_sistema()

# Self smp vai referenciar a instancia direciona para qual atributo, pessoa, etc esta sendo referido