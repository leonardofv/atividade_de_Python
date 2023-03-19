# Ler 10 números inteiros e no final mostrar a quantidade de pares e ímpares.

contador = 1
par = 0
impar = 0

while contador <= 10:

    num = int(input(f'Digite o {contador} número: '))

    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    contador += 1

print('Dos números digítados {} são pares e {} são ímpares'.format(par,impar))
