#Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km rodados? '))
totaldias = dias * 60
totalkm = km * 0.15
totalapagar = totaldias + totalkm
print('O total a pagar pelo aluguel do carro é R${:.2f}'.format(totalapagar))