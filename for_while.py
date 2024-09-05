#for in
banana = 'Banana'

for letra in 'python':
    print(letra)
    if letra.upper() in banana:
        print(f'achou {letra}')
    else:
        print(f'nao achou {letra}')

#range
list[range(4)]
for i in range(4):
    print(i)

for numero in range(0,51,5):
    print(numero, end=' ')

#while
opcao = None
while opcao != 0:
    try:
        opcao = int(input('[1] Depositar\n [2] Sacar\n [0] Sair'))
        if opcao == 1:
            print('depositar')
        elif opcao == 2:
            print('sacar')
        elif opcao == 0:
            print('saindo')
        else:
            print('Opção inválida. Por favor, tente novamente.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')