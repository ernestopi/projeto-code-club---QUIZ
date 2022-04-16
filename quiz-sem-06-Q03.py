score = int(0)

estado = input('QUAL O MELHOR ESTADO DO BRASIL PARA MORAR?').strip().upper()
if estado == ('PIAUI'):
    print()
elif estado != ('VOCÊ PRECISA CONHECER O PIAUI'):
    print()
else:
    print()
if estado == 'PIAUI':
    score = score + 1

selecao = input('QUAL SELEÇÃO TEM MAIS TÍTULOS DA COPA DO MUNDO?').upper()
if selecao == 'BRASIL':
    print()
elif selecao == 'ITÁLIA':
    print()
elif selecao == 'ARGENTINA':
    print()
else:
    print()

if selecao == 'BRASIL':
    score = score + 1

print(f'SUA PONTUAÇÃO FOI DE {score} PT(S)')

if score == 2:
    print('muito bem!')
else:
    print('tente novamente')