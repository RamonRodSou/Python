#Receba uma temperatura em farenheit e exiba em graus celsius.
# C = 5 * F -  32 / 9 

temp_farenheit = float(input('Digite uma temperatura em graus farenheit: '))
temp_celsius = 5 * ((temp_farenheit - 32) / 9 )

print(f'a temperatura em graus celsius é {temp_celsius}')