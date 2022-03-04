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
# Arquivo: exercicios3\capitulo 04\exercicio-04-02.py
##############################################################################

#04-02

vel_carro = float(input('Digite a velocidade do seu carro (km/h): '))
vel_limite = 80
multa = 5
cobranca_multa = (vel_carro - vel_limite) * 5

if vel_carro > vel_limite:
    print (f'Você foi multado em R${cobranca_multa:.2f}!')
else:
    print ('Sua velocidade está dentro do limite permitido, boa viagem!')

#04-03

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

if x > y and x > z:
    maior = x
elif y > x and y > z:
    maior = y
else:
    maior = z

if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else:
    menor = z

print (f'O maior e o menor número são respectivamente: {maior} e {menor}.')

#04-04

salario_atual = float(input('Digite seu salário atual (R$): '))


if salario_atual > 1250:
    aumento = (salario_atual * 0.1)
else:
    aumento = (salario_atual * 0.15)

print (f'Seu aumento salarial será de R${aumento:.2f}.')

#04-06

distancia = float(input('Digite a distância que você pretende percorrer (km): '))

if distancia <= 200:
    preco_passagem = (distancia * 0.5)
else:
    preco_passagem = (distancia * 0,45)

print (f'O preço da sua passagem é de R${preco_passagem:.2f}.')


#04-08

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

operacao = (input('Digite a operação que deseja realizar (+,-,* ou /): '))

if operacao == '+':
    execute = x + y
elif operacao == '-':
    execute = x - y
elif operacao == '*':
    execute = x * y
elif operacao == '/':
    execute = x / y
else:
    execute = 'Operação inválida!'

print (f'Resultado: {execute}.')

#04-09

valor_casa = float(input('Digite o valor da casa a comprar (R$): '))
salario = float(input('Digite o valor do seu salário (R$): '))
anos_pagar = float(input('Digite em quantos anos você pretende pagar o empréstimo: '))

conv_meses = (anos_pagar * 12) #conversão de anos a pagar para meses

valor_prestacao = (valor_casa / conv_meses)

if valor_prestacao > (salario * 0.3):
    print ('Infelizmente o empréstimo não está disponível para você.')
else:
    print (f'O empréstimo está disponível para você. O valor da prestação é R${valor_prestacao:.2f}.')

#04-10

kwh_consumidos = float(input('Digite a quantidade de KW/h consumidos: '))
instalacao = (input('Digite o tipo de instalação (R - residência, I - indústria ou R - comércio): '))

if instalacao == 'R' and kwh_consumidos <= 500:
    valor = 0.4
elif instalacao == 'R' and kwh_consumidos > 500:
    valor = 0.65

if instalacao == 'C' and kwh_consumidos <= 1000:
    valor = 0.55
elif instalacao == 'C' and kwh_consumidos > 1000:
    valor = 0.6

if instalacao == 'I' and kwh_consumidos <= 5000:
    valor = 0.55
elif instalacao == 'I' and kwh_consumidos > 5000:
    valor = 0.6


preco = kwh_consumidos * valor

print (f'O valor a pagar é de R${preco:.2f}.')