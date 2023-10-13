class Pessoas:

    possui_olho = True
    pussui_boca = True
    raca = 'ser humana'

    def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade
    
    def return_nome(self):
         return self.nome
    
    def logar_sistema(self):
        print(f'{self.return_nome()} Está logando no sistema')

p1 = Pessoas('Ramon Rodrigues', 30)
p2 = Pessoas('Samara Rodrigues', 31)
print(f'{p1.nome} é {Pessoas.raca}')  # quando muda um Atributo de instancia, muda apenas dela

p1.nome = 'Antonio Rodrigues'

print(f'Mudando o Nome e Ramon para {p1.nome} que é {Pessoas.raca}')
print(f'{p2.nome} é {Pessoas.raca}')

Pessoas.raca = 'Filhos de Deus'       # Mudando o atributo da Classe, muda de todas as instancias dela
print(f'{p1.nome} é {Pessoas.raca}')
print(f'{p2.nome} é {Pessoas.raca}')



