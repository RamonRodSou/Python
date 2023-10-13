#Receba um numero e exiba se ele é positivo ou negativo

num = float(input('Digite um valor: '))

if num > 0:
    print(f'{num} é numero positivo')
elif num < 0:
    print(f'{num} é numero negativo')
else:
    print(f'{num} é numero neutro')