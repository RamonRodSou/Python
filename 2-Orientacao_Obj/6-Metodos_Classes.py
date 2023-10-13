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

    @classmethod                # quer dizer que esse metodo pertencia a Classe pessoas e consigo chamar direto
    def andar(cls, velocidade): # cls aponta para a Classe
        print(f'Estou andando a {velocidade} km/h')

Pessoas.andar(10)