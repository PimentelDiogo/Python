curso = 'python'
saldo = 500
print(curso[0])
print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.swapcase())
print(curso.find('h'))
print(curso.replace('p','j'))
print(curso.strip())#remove espaco em branco
print(curso.lstrip())#remove espaco em branco esquerda
print(curso.rstrip())#remove espaco em branco direita
print(curso.center(10,'*'))#add caracter para centralizar a string/texto
print('.'.join(curso))#passa item a item e add o caracter

#interpolação
print(f'{curso} e muito legal')
print('%s'%curso)
print('Meu curso de {}'.format(curso))
print(f'Meu curso de {curso} custa {saldo:.1f}')
print(curso[::-1])

#multi-linha / triplas
print('''
    minhas frutas favoritas sao:
    maca
    banana
    abacaxi''')