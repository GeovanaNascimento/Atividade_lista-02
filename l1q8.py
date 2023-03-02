#faça um programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.calcule e mostre o total do seu salario no referido mes
#calcule e mostre o total do seu salario no referido mes

#entradas
valor_hora_tralho = float (input('Qual o valor de hora de trabalho: '))
quantidade_horas_trabalhadas = float (input ('Qual a quantidade de horas trabalhadas: '))

#processamento
salario_mensal = valor_hora_tralho * quantidade_horas_trabalhadas

#saida
print ('O valor do salario mensal é: {}'. format(salario_mensal))

