#Receba 3 numeros inteiros e exiba o maior deles.

n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
n3 = int(input('Digite o terceiro numero inteiro: '))

if (n1 > n2) and (n1 > n3):
    print(f'n1: {n1}, é maior que n2: {n2} e maior que n3: {n3}')
elif (n2 > n1) and (n2 > n3):
    print(f'n2: {n2}, é maior que n1: {n1} e maior que n3: {n3}')
elif (n3 > n1) and (n3 > n2):
    print(f'n3: {n3}, é maior que n1: {n1} e maior que n2: {n2}')
else:
    print(f'n1: {n1}, n2: {n2} e n3: {n3}, sao iguais')