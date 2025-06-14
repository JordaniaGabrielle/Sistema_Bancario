def estetica():
    print(20*'=+=')


estetica()

print('Bem-vindo ao banco Santander\nQual operação gostaria de realizar?')
menu = """
[D] Depósito
[S] Saque
[E] Extrato
[T] Saldo
[F] Sair
"""
valor = 0
cont = 0
limite = 500
limite_saque = 3
deposito_conta_bancaria = 0
historico = []


def Deposito(deposito_conta_bancaria):
    global valor

    if deposito_conta_bancaria > 0:
        valor += deposito_conta_bancaria

        historico.append(f'{deposito_conta_bancaria} Depositado')
    else:
        print('Erro ao depositar, O valor é negativo.')


def Saque(saque):
    global valor, cont

    valor_insuficiente = saque > valor

    limite_saq = cont >= limite_saque

    limite_valor = saque > limite

    if valor_insuficiente:
        print(f'O valor: R$ {saque} excede o valor existente '
              f'na conta bancária')

    elif limite_saq:
        print('Limite de saque diário excedido')

    elif limite_valor:
        print('O limite diário de R$ 500 foi atingido')

    elif saque <= valor:
        valor -= saque
        print(f'Debitado {saque}')

        historico.append(f'{saque} Sacado')
        cont += 1


while True:
    opcao = input(menu).upper()
    estetica()
    # Deposito
    if opcao == 'D':
        deposito_conta_bancaria = float(input('Valor do depósito: '))

        Deposito(deposito_conta_bancaria)

    # Saque
    elif opcao == 'S':
        saque = float(input('Valor de Saque: '))
        Saque(saque)

    # Extrato
    elif opcao == 'E':
        print('\nEXTRATO')
        for operacao in historico:
            print(operacao)
        estetica()
        print('Pressione enter para continuar...\n')
        input()
    # Saldo
    elif opcao == 'T':
        print(f'Saldo: R$ {valor}')
    # Sair
    elif opcao == 'F':
        break
