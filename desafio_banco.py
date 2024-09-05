menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
'''
saldo = 1000
limite = 500
numero_saque =0
extrato = ''
LIMITE_SAQUES=3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor_deposito = float(input('Quanto quer depositar? '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito de R${valor_deposito:.2f}\n'
        elif valor_deposito <= 0:
            print('Tente novamente')

    elif opcao == '2':
        valor_saque = float(input('Quanto quer sacar? '))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print(f'Operação falhou! O valor do saque excede o limite de R${limite}.')
        elif excedeu_saque:
            print('Operação falhou! Você atingiu o limite de saques diários.')
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque de R${valor_saque:.2f}\n'
            numero_saque += 1
    elif opcao == '3':
        print('********** Extrato **********')
        print(f'Saldo: R${saldo:.2f}')
        print(f'Extrato:{extrato}\nLimite por saque: R${limite:.2f}\nSaques: {numero_saque}')
        print('************************************')
    elif opcao == '0':
        break
    else:
        print('Operação falhou! Selecione uma opção válida.')