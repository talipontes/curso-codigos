
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

# 01-02

print (10 + 20 * 30)

print (42 / 30)

print (int (42 / 30))

print ((94 + 2) * 6 - 1)

# 02-02

print (((10%3) * 10**2) + (1-10 * (4/2)))

# 02-03

nome = 'Talita Pontes'

print (f'Meu nome é {nome}.')

#02-04

a = 3
b = 5

print (2*a * 3*b)

# SE EU QUISER QUE O USUÁRIO INFORME OS VALORES DE 'a' E 'b':

a = float (input ('\nDigite o valor de a: '))

b = float (input ('\nDigite o valor de b: '))

cálculo = 2 * a * 3 * b

print (f'\nO resultado de 2a x 3b é: {cálculo:.0f}.')

#02-05

a = float (input ('Digite o valor de a: '))

b = float (input ('Digite o valor de b: '))

c = float (input ('Digite o valor de c: '))

soma = a + b + c

print (f'\nA soma de a, b e c equivale a: {soma:.0f} .')

#02-06

salario = 750

aumento = 0.15

print (salario + (salario * aumento))

# Outra forma, com o usuário digitando as informações:

salario = float (input ('Digite aqui o valor do salário (R$): '))

aumento = float (input ('Digite aqui o valor do aumento (%): '))

aumento_em_porcentagem = (aumento / 100) * salario

salario_pos_aumento = aumento_em_porcentagem + salario

print (f'\nO salário atualizado com o aumento é de {salario_pos_aumento} reais.')