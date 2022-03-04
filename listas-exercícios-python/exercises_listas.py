"""Exercício 1: 
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser: 
>>> Elemento 1 na posição 0 
>>> Elemento 3 na posição 1 
>>> Elemento 6 na posição 2 
>>> Elemento “H” na posição 3""" 

metais = ['Rutênio', 'Cobre', 'Vanádio', 'Cobalto', 'Zinco']

print (f'Elemento {metais [0]} na posição 0' )
print (f'Elemento {metais [1]} na posição 1' )
print (f'Elemento {metais [2]} na posição 2' )
print (f'Elemento {metais [3]} na posição 3' )
print (f'Elemento {metais [4]} na posição 4' )

"""Exercício 2: 
Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser 
>>> [[7,7,7], “H”, 6, 3, 1]""" 

lista = [34, 56, 'world', [1,2,3], 45, 'Earth', [6,54], 43, 76, 'cloud']

lista.reverse()

print (lista)

"""Exercício 3: 
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. 
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser 
>>> O maior elemento é 8 e está na posição 3 
>>> O menor elemento é 3 e está na posição 4 
Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição."""

numeros = [6, 45, 8, 89,102,34]

maior = max(numeros)
posicaomaior = numeros.index(maior)
menor = min(numeros)
posicaomenor = numeros.index(menor)

print (f'O maior número é o {maior} e está na posição {posicaomaior}.')
print (f'O maior número é o {menor} e está na posição {posicaomenor}.')

"""Exercício 4: 
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da 
média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída: 
>>> Meses com temperatura acima da média anual de 35,5°: 
>>> 1 – janeiro 
>>> 3 – março 
>>> 6 – junho """

temperaturas = [ float(input('Digite a temperatura média do mês ' + str(mes)) ) for mes in range (1,12+1)]

print (temperaturas)

print ('A maior temperatura foi',max(temperaturas), '°C e aconteceu no mês',temperaturas.index(max(temperaturas))+1)
print ('A menor temperatura foi',min(temperaturas), '°C e aconteceu no mês',temperaturas.index(min(temperaturas))+1)


"""Exercício 5: 
Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após 
o elemento 6000 na lista acima. O resultado final deverá ser: 
>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] """

lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

lst.insert (2,7000)
print (lst)

"""Exercício 6: 
Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser 
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]""" 

lst = ['Eu', ' ', 'gosto', ' ', 'de', ' ', 'jogar']

lst = list(filter((' ').__ne__, lst))

print (lst)

#OUTRA FORMA 

lst = ['Eu', ' ', 'gosto', ' ', 'de', ' ', 'jogar']
queroremover = ' '

try:
    while True:
        lst.remove(queroremover)
except ValueError:
    pass

print (lst)

"""Exercício 7: 
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro. 
Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int. """ 

strings = ['1', '7', '99', '15']

intlist = [int(i) for i in strings]
print (intlist)

