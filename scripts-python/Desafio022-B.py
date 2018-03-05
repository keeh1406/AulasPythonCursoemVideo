# Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))