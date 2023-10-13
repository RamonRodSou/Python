# x = []

# for i in range (0, 10):    # para i dentro de um range de 0 a 10
#     if i % 2 == 0:         # se a sobra da divisao for divisivel  ( modulo ) por 2 == 0
#         x.append(i)        # add dentro da lista apenas os pares
#     print(x)              

# add i, opara cada valor de ir em range
x = [i for i in range(0,10) if i % 2 == 0 ]
print(x)  