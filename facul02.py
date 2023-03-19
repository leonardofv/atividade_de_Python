#Usuário deverá acertar a senha do cartão.

senha = 'senha123'

tentativa = input('Digite sua senha do cartão: ')

while tentativa != senha:

    print('Senha invalida. Tente digita-la novamente')
    tentativa = input('Digite sua senha do cartão: ')

print('Senha Correta')

#-----------------------------------------------------------------------------------------------------------------------

senha2 = 'senha321'
acertou = False

while not acertou:
    op = input('Digite a senha do cartão: ')

    if op == senha2:
        print('Senha Correta')
        acertou = True
    else:
        print('Tente novamente')
