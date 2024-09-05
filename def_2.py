def somar(a,b):
    return a+b

def resultado(a,b,funcao):
    resultado= funcao(a,b)
    print(f'resultado {a} + {b} = {resultado}')

resultado(1,2,somar)