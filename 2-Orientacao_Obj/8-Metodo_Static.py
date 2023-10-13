#Metodo static também pode ser chamado apenas pela classe, nao precisa da instancia
#Porem ele é apenas um metodo utilitario, nao podendo
#Acessar, modificar, nenhum atributo ou metodo de classe
#Pode ser acessado pela classe, mas nao tem nao enchegar nada da classe

class Pessoas:
    possui_olhos = True
    possui_boca = True
    raca = 'Ser humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def retorna_nome(self):        #Self Aponta a Instancia
        return self.nome
     
    def logar_sistema(self):
        print(f'{self.returna.nome()} Esta logando no sistema')

    @staticmethod
    def adulto(idade):
        if idade >= 18:
            return True
        return False

print(Pessoas.adulto(21))