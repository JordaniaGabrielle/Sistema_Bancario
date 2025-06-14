def estetica():
    print(20*'=+=')

estetica()

print('Bem-Vindo ao banco Santader\nQual operação gostaria de realizar')
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
deposito_conta_bacaria = 0
historico = []

def Deposito(deposito_conta_bancaria):
    global valor

    if deposito_conta_bacaria > 0:
        valor += deposito_conta_bacaria

        historico.append(f'{deposito_conta_bacaria} Depositado')
    else:
        print('Erro ao depositar, O valor é negativo.')

def Saque(saque):
    global valor, limite_saque, cont

    valor_insuficiente = saque > valor

    limite_saq = cont >= limite_saque

    limite_valor = saque > limite

    if valor_insuficiente:
        print(f'O valor:{saque}R$ excede o valor existente na conta bancaria')

    elif limite_saq:
        print('Limite de saque diario excedido')
        
    elif limite_valor:
        print('O limite diario R$ foi atingido')
        
    elif saque <= valor :
        valor -= saque
        print(f'Debitado {saque}')

        historico.append(f'{saque} Sacado')
        cont += 1

while True:
    opcao = input(menu).upper()
    estetica()
    # Deposito
    if opcao == 'D':
        deposito_conta_bacaria = float(input('Valor do deposito:  '))

        Deposito(deposito_conta_bacaria)

    # Saque
    elif opcao == 'S':
        saque = float(input('Valor de Saque:  '))
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
        print(f'Saldo:{valor}R$')
    # Sair
    elif opcao == 'F':
        break
