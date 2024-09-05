def ola_mundo():
    print('ola mundo')

def ola_nome(nome):
    print(f'ola {nome}')

ola_mundo()
ola_nome('diogo')

#args kwargs
def somar(*args):
    print(args)
somar(1,2,3,4,5,6,7,8,9,10)

def nome_completo(**kwargs):
    print(kwargs)
nome_completo(nome='diogo', sobrenome='pimentel')

def exibir_poema(data_extenso, *args, **kwargs):
#args será separado por virgua, e o kwargs ele é tudo que for chave e valor
    texto=' '.join(args)
    meta_dados='\n'.join([f'{chave.title}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n{texto}\n{meta_dados}'
    print(mensagem)

exibir_poema('domingo, 01 de janeiro de 2021', 'eu amo python', 'estou gostando de python', status='aprovado', autor='diogo', ano='2021')