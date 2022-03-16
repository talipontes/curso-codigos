"""Exercício 1: 
Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo: 
Alunos matriculados em inglês: 
João Alves dos Santos 
Maria Magalhães 
Antônio da Silva Ferreira 
José Júnior Jarbas 
Henrique da Silva Sauro 
Joaquina Ferreira da Silva 
Fabiana Aparecida Bianco 
Marrone Gutierres 
Carlos Magno Farad 
Antônio da Silva Júnior Amaral 

Alunos matriculados em francês: 
João Alves dos Santos 
Antônio da Silva Ferreira 
Fernanda Abdala Mohamed 
Abner Mignon Alib 
Alisson Figueiredo 
Henrique da Silva Sauro 
Maria Magalhães 
Marrone Gutierres 
Joaquina Ferreira da Silva 

Faça um programa que responda as seguintes perguntas: 
Quantos alunos estão matriculados na escola, no total? 
Quantos e quais estão matriculados APENAS em INGLES? 
Quantos e quais estão matriculados APENAS em FRANCES? 
Quantos e quais estão matriculados EM AMBOS os cursos? 
Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos? """

ingles = ['João Alves dos Santos', 'Maria Magalhães', 'Antônio da Silva Ferreira', 'José Júnior Jarbas', 'Henrique da Silva Sauro',
'Joaquina Ferreira da Silva', 'Fabiana Aparecida Bianco', 'Marrone Gutierres', 'Carlos Magno Farad', 'Antônio da Silva Júnior Amaral']

frances = ['João Alves dos Santos', 'Antônio da Silva Ferreira', 'Fernanda Abdala Mohamed', 'Abner Mignon Alib', 'Alisson Figueiredo', 
'Henrique da Silva Sauro', 'Maria Magalhães', 'Marrone Gutierres', 'Joaquina Ferreira da Silva']

set_ingles = set(ingles)
set_frances = set(frances)

totalescola = set_ingles.union(set_frances)
print (f'Total de alunos da escola: {len(totalescola)}.')

intersecao = set_ingles.intersection (set_frances)
print (f'Total de alunos em ambos os cursos: {len(intersecao)}.') 

matingles = set(ingles)
print (f'Total de alunos matriculados no curso de ingês: {len(matingles)}.')

matfrances = set(frances)
print (f'Total de alunos matriculados no curso de francês: {len(matfrances)}.')

somenteingles = (matingles - intersecao)
print (f'Total de alunos matriculados SOMENTE no curso de inglês: {len(somenteingles)}.')

somentefrances = (matfrances - intersecao)
print (f'Total de alunos matriculados SOMENTE no curso de francês: {len(somentefrances)}.')



"""Exercício 2: 
Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo: 
>>> Digite um estado: SP 
>>> O nome completo do estado é São Paulo."""

estados = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'ES': 'Espírito Santo', 'MG': 'Minas Gerais'}

siglaestado = input('Digite a sigla de um estado da região Sudeste: ')

print (f'O nome completo do estado é {estados[siglaestado]}.')


"""Exercício 3: 
Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário 
>>> {“matemática”: 81, “física”: 83, “química”: 87}  
a saída deve ser  
>>> {“química”: 87, “física”: 83, matemática”: 81}"""

dicionario = {'mecânica clássica': 457, 'eletromagnetismo': 45, 'ondas': 54, 'ótica': 43, 'quântica': 9}

#em ordem crescente

ordenado_cresc = {k: v for k, v in sorted (dicionario.items(), key = lambda item: item [1])}

print (ordenado_cresc)

# em ordem decrescente:

ordenado_decresc = {k: v for k, v in sorted (dicionario.items(), key = lambda item: item [1], reverse = True)}

print (ordenado_decresc)

"""EXERCÍCIO 4: 
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dado o dicionário 
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”} 
A saída deverá ser 
>>> {1: 8, 2: 4, 3: 6}"""

dicionario = {1: 'Rutherford', 2:'Bohr', 3: 'Dalton', 4: 'Schrodinger', 5: 'Thompson'}

k = {1: len('Rutherford'), 2: len('Bohr'), 3: len('Dalton'), 4: len('Schodinger'), 5: len('Thompson')}
print (k)

# UMA MANEIRA MELHOR:

resultado = dict()

for chave, valor in dicionario.items():
    resultado [chave] = len(valor)

print (resultado)

"""EXERCÍCIO 5: 
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário 
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80} 
A saída deve ser 
>>> Nota máxima -> Júnior : 80 
>>> Nota mínima -> Theodoro : 20"""

entrada = {'Theodoro': 34, 'Márcia': 87, 'Júnior': 57, 'Ana': 67}

# Coletando todos os valores do dicionário e transformando-os em uma lista
valores = list(entrada.values())

# Valores máximo e mínimo da lista
valor_max = max(valores)
valor_min = min(valores)

# Índices (posições) máximo e mínimo dos respectivos valores
indice_max = valores.index(valor_max)
indice_min = valores.index(valor_min)

# A partir do índice, conseguimos extrair o nome transformando as chaves dos dicionários em uma lista
print(f"Nota máxima -> {list(entrada.keys())[indice_max]}: {valor_max}")
print(f"Nota mínima -> {list(entrada.keys())[indice_min]}: {valor_min}")