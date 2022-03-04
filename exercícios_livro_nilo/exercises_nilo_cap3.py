##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 02\exercicio-02-01.py
##############################################################################


#03-02

a = 4
b = 10
c = 5.0
d = 1
f = 5

if a == c:
    status = 'True'
else:
    status = 'False'

print (status)

if a < b:
    status = 'True'
else:
    status = 'False'

print (status)

if d > b:
    status = 'True'
else:
    status = 'False'

print (status)

if c != f:
    status = 'True'
else:
    status = 'False'

print (status)

if a == b:
    status = 'True'
else:
    status = 'False'

print (status)

if b > a:
    status = 'True'
else:
    status = 'False'

print (status)

if c >= f:
    status = 'True'
else:
    status = 'False'

print (status)

if f >= c:
    status = 'True'
else:
    status = 'False'

print (status)

if c <= c:
    status = 'True'
else:
    status = 'False'

print (status)

if c <= f:
    status = 'True'
else:
    status = 'False'

print (status)

#03-04

minimo_imposto = 1200
salario = float(input('Digite o valor do seu salário (R$): '))

if salario > minimo_imposto:
    status = 'Você terá que pagar imposto.'
else:
    status = 'Você não precisa pagar imposto.'

print (status)

#03-06

materia1 = float(input('Digite o valor da sua nota: '))
materia2 = float(input('Digite o valor da sua nota: '))
materia3 = float(input('Digite o valor da sua nota: '))

media_meta = 7

media_aluno = (materia1 + materia2 + materia3) / 3

if media_aluno > media_meta:
    status = 'Parabéns, você foi aprovado (a)!'
else:
    status = 'Poxa, infelizmente você foi reprovado (a)!'

print (status)

#03-07

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2

print (soma)

#03-08

medida_metros = float(input('Digite a medida em metros (m): '))

medida_milimetros = medida_metros * 1000

print (f'{medida_metros:.1f} metros equivalem a {medida_milimetros:.0f} milímetros.')

#03-09

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

dias_segundos = dias * 86400
horas_segundos = horas * 3600
minutos_segundos = minutos * 60

total_segundos = dias_segundos + horas_segundos + minutos_segundos + segundos

print (f'Convertido para segundos, o total é igual a: {total_segundos} .')

#03-10

salario = float(input('Digite aqui o valor do seu salário atual (R$): '))
p_aumento = float(input('Digite aqui a porcentagem do aumento (%): '))

valor_aumento = (p_aumento/100) * salario

novo_salario = valor_aumento + salario

print (f'Seu salário sofreu um aumento de {valor_aumento:.2f} reais, passando de {salario:.2f} para {novo_salario:.2f} reais.')

#03-11

preco_real = float(input('Digite o preço da mercadoria (R$): '))
p_desconto = float(input('Digite o percentual de desconto (%): '))

valor_desconto = (p_desconto/100) * preco_real

preco_atualizado = preco_real - valor_desconto

print (f'Essa mercadoria sofreu um desconto de {p_desconto}%, que equivale a {valor_desconto:.2f} reais.')
print (f'O novo preço dessa mercadoria é de {preco_atualizado:.2f} reais.')

#03-12

distancia = float(input('Digite a distância que será percorrida (km): '))
velocidademedia = float(input('Digite a velocidade média esperada para a viagem (km/h): '))

tempo = (distancia / velocidademedia)

tempo_horas = int(tempo)
tempo_minutos = int(distancia % velocidademedia)

print (f'O tempo estimado para a viagem é de aproximadamente {tempo_horas} horas e {tempo_minutos} minutos.')

#03-13

temp_c = float(input('Digite a temperatura em graus Celsius (°C): '))

temp_f = ((9 * temp_c ) / 5) + 32

print (f'{temp_c}°C equivale a {temp_f}°F.')

#03-14

km_percorridos = float(input('Digite a quantidade de quilometros percorridos (km): '))
dias = float(input('Digite quantos dias você ficou com o carro: '))

preco_diaria = 60
preco_km = 0.15

valor_km = km_percorridos * preco_km
valor_diaria = dias * preco_diaria

valor_total = valor_km + valor_diaria

print (f'O valor total a pagar é de R${valor_total}.')

#03-15

cigarros_por_dia = float(input('Digite a quantidade de cigarros fumados por dia: '))
anos_fumando = float(input('Digite por quantos anos você é fumante: '))

convr_anos_dia = (anos_fumando * 365) #conversão para dias de quantos anos ele é fumante

red_min = (cigarros_por_dia * 10) * convr_anos_dia #quantos minutos de vida ele perdeu fumando

convr_min_dia = int(round(red_min / 1440)) #conversão dos minutos perdidos para dias


print (f'Redução do tempo de vida: {convr_min_dia} dias.')

