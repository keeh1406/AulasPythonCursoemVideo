# Cire um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção inteira
# EX: Digite um número: 6.127
# EX: O número 6.127 tem a parte inteira 6.

num = float(input('Digite um valor: '))
print('O valor digitado foi {}'.format(num))
print('A sua porção inteira é {}'.format(int(num)))