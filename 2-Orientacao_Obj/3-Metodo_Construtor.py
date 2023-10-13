class Pessoas:
    def __init__(self, nome, idade, cpf):    #construtor da classe Metodo que será chamado sempre que inicializarmos uma instancia de class
        print(f'{nome} | {idade} | {cpf}')

    def logar_sistema(self):
        print(f'Estou Logando no sistema')

p1 = Pessoas('Ramon Rodriues', 30, '00022233332')