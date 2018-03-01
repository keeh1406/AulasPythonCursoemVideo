#Faça um programa que leia um número inteiro e mostre
#o seu sucessor e seu antecessor

n = int(input('Digite um valor: '))
antecessor = n - 1
sucessor = n + 1

print('O antecessor de {} é {}'.format(n, antecessor))
print('O sucessor de {} é {}'.format(n, sucessor))
