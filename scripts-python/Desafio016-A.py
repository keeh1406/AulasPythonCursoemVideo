# Cire um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção inteira
# EX: Digite um número: 6.127
# EX: O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {}'.format(num))
print('A sua porção inteira é {}'.format(trunc(num)))