# Um profesor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do ecolhido.

from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
listaalunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(listaalunos)
print('O aluno escolhido foi {}'.format(escolhido))