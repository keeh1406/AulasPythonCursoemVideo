from math import sqrt
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {}".format(num, (raiz)))
print("A raiz de {} arredondado com duas casas decimais é igual a {:.2f}".format(num, (raiz)))
print("A raiz de {} arredondado para cima é igual a {}".format(num, math.ceil(raiz)))
print("A raiz de {} arredondado para baixo é igual a {}".format(num, math.floor(raiz)))
