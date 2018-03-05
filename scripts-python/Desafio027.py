# Faça um programa de leia o nome completo de uma pessoa
# e mostre em seguida o primeiro e o último nome separados
# Ex: Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = str(input('Digite seu nome completo: ')).strip()
nomecortado = nome.split()
print('Seu primeiro nome é: {}'.format(nomecortado[0]))
print('Seu último nome é: {}'.format(nomecortado[len(nomecortado)-1]))
