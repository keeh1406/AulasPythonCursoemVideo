#Faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de
#tita, pinta uma area de 2m2.

largura = float(input('Qual é a largura da sua parede? '))
altura =  float(input('Qual é a altura da sua parede? '))
area = largura * altura
print('Sua parede tem a dimensão {}x{} e sua área é de {}m2'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, será necessário {}L de tinta'.format(tinta))