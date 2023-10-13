#Sempre que for criado um @classmethod sempre vai receber um CLS
#E atraves do CLS, vc pode ver, modificar, alterar, apagar (CRUD)

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
    def andar(cls): # cls aponta para a Classe
        cls.possui_boca = False

print(Pessoas.possui_boca)
Pessoas.andar() #Chamnando o metodo andar, ele vai criar ou alterar atributos
print(Pessoas.possui_boca)

#Dentro de @classmethod posso criar um atributo de classe
#E sempre que for chamado os metodos dentro de classmethod
#Vai ser criar um novo atributo de classe ou alterado