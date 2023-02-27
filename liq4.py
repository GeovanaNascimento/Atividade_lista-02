#faça um programa que peça as 4 notas bimestrais e mostre a media.
#somar as 4 notas por 4

#entrada das notas
nota_1 = float (input ('Digite sua primeira nota: '))
nota_2 = float (input ('Digite sua segunda nota: '))
nota_3 = float (input ('Digite sua terceira nota: '))
nota_4 = float (input ('Digite sua Quarta nota: '))
nota_5 = float (input ('Digite sua quinta nota: '))
nota_6 = float (input ('Digite sua sexta nota: '))
nota_7 = float (input ('Digite sua setima nota: '))
nota_8 = float (input ('Digite sua oitava nota: '))

#calculo da media
media_do_1bimestre = (nota_1 + nota_2)/2
media_do_2bimestre = (nota_3 + nota_4)/2
media_do_3bimestre = (nota_5 + nota_6)/2
media_do_1bimestre = (nota_7 + nota_8)/2

#exibir o resultado
print ('Sua nota no primeiro bimestre é: ', media_do_1bimestre)
print ('Sua nota no segundo bimestre é: ', media_do_2bimestre)
print ('Sua nota no terceiro bimestre é: ', media_do_3bimestre)
print ('Sua nota no quarto bimestre é:', media_do_4bimestre)

