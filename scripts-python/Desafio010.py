#Crie um programa que leia quanto dinheiro uma pessoa
#temna cartera e mostre quantos dólares ela pode comprara
#considere U$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você ode comprar U${:.2f}'.format(real, dolar))