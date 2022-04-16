time_de_futebol = input('PARA QUAL TIME VOCÊ TORCE?').lower().strip()
if time_de_futebol == 'são paulo':
    print('VOCÊ TEM ÓTIMO GOSTO!')
elif time_de_futebol == 'flamengo':
    print('SEU GOSTO É PÉSSIMO')
elif time_de_futebol == 'santos':
    print('GOSTA DE SOFRER!')
else:
    print('VOCÊ TEM QUE APRENDER A TORCER')

idade = int(input('QUAL A SUA IDADE ? : '))
if idade <= 16:
    print('ADOLESCENTE')
else:
    print('ADULTO')

