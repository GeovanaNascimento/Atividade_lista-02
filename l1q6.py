#importa o valor de pi e a funçao de potencia (pow) da biblioteca math
from math import pi, pow

#Faça um programa que peça o raio de um circulo, calcule e mostre sua area.
#área do circulo = 2 * pi * r * r
#entrada
raio_do_circulo = float(input('Informe o tamanho do raio do circulo: '))

#processamento
area_do_circulo = 2 * pi * pow(raio_do_circulo,2)


#resposta
print('A área do circulo é {:.2f}' .format(area_do_circulo))
