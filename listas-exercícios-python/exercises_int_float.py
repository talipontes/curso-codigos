"""Exercício 1: 
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações: 
A soma de A e B; 
A diferença quando se subtrai B de A; 
O produto (multiplicação) entre A e B; 
O quociente (parte inteira da divisão) quando se divide A por B; 
O resto da divisão entre A e B; 
O resultado de log10 de A; 
O resultado de A elevado a B;""" 


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print (a + b)

print (b - a)

print (a * b)

print (a / b)

print (a % b)

import math
print (math.log10(a))

print (a ** b)


"""Exercício 2: 
Faça um programa que receba a base e altura de um triângulo e imprima a área dele.""" 

base = float(input('Digite o valor da base do triângulo (m): '))
altura = float(input('Digite o valor da altura do triângulo (m): '))

area = (base * altura) / 2

print (f'A área do triângulo é de {area:.2f} metros quadrados.')

"""Exercício 3: 
No exercício acima você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.""" 

lado1 = float(input('Digite o valor do primeiro lado do triângulo (m): '))
lado2 = float(input('Digite o valor do segundo lado do triângulo (m): '))
lado3 = float(input('Digite o valor do terceiro lado do triângulo (m): '))

l = (lado1 + lado2 + lado3) / 2
calc = ( l * (l - lado1) * (l - lado2) * (l - lado3))

import math
area = math.sqrt(calc)

print (f'A área do triângulo é de {area:.2f} metros quadrados.')

#Exercício 4: 
# Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário. 

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = (peso / (altura ** 2))

print (f'Seu Índice de Massa Corporal (IMC) é igual a: {imc:.2f} kg/m².')