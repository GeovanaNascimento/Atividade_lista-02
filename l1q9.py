#9. Faça um programa que peça a temperatura em graus fahrenheit, transforme e mostre a temperatura em graus celsius.
#°C = 5 ((°F-32) / 9).
#entrada
temperatura_Fahrenheit = float (input('Temperatura em farenheit: '))

#processamento
#°F = (9 * °C) / 5 + 32
temperatura_em_celcius = 5 * (temperatura_Fahrenheit - 32) / 9

#saida
print ('A temperatura {: .1f} °F é igual a {: .1f} °C '. format (temperatura_Fahrenheit, temperatura_em_celcius))
