saldo=500
def sacar(valor):   
    global saldo
    if valor <= saldo:
        saldo -= valor
        print(saldo)
        return saldo
    elif valor > saldo:
        print('saldo insuficiente')
        return None
sacar(400)

def depositar(valor):
    deposito= 'depositado'if saldo + valor else 'insuficiente'
    print(f'{deposito} saldo de {valor}')
depositar(200)