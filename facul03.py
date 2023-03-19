# Receber a idade e opinião de 20 espectadores, calcular e imprimir a quantidade de pessoas que responderam regular,bom e excelente.

cont = 1
contR = 0
contB = 0
contE = 0

while cont <= 10:

    idade = int(input('Digite sua idade: '))

    print('Agora por favor responda o que achou do filme')

    print('-> 1 para Regular')
    print('-> 2 para Bom')
    print('-> 3 para Otimo')

    op = int(input('Qual sua opinião: '))

    if op == 1:
        contR += 1
    elif op == 2:
        contB += 1
    elif op == 3:
        contE += 1

    cont += 1

print(f'A quantidade de pessoas que responderam REGULAR foram {contR}')
print(f'A quantidade de pessoas que responderam BOM foram {contB}')
print(f'A quantidade de pessoas que responderam EXCELENTE foram {contE}')
