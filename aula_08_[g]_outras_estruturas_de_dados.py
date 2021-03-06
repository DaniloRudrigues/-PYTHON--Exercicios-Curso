# -*- coding: utf-8 -*-
"""Aula 08 - [G] - Outras Estruturas de Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/DaniloRudrigues/57c9052d7e2e76cc5b516469e10e8504/aula-08-g-outras-estruturas-de-dados.ipynb

# Exercícios

## 1 - Dada a lista a seguir, crie uma segunda lista apenas com os itens na mesma ordem mas sem repetição.
```python
l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
```
"""

l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
var1 = set(l)
print(var1)

"""## 2 - Construa um dicionário para mapear o número do CEP dos seus colegas para o endereço da casa de cada um. Faça também um programa no qual o usuário insere o número do CEP e recebe como resposta o endereço."""

#---CRIAÇÃO DA LISTA DE ENDEREÇOS---
cep = {
    '10.000-123':'Rua A',
    '20.123-456':'Rua B',
    '30.756-987':'Rua C',
    '40.123-895':'Rua D',
    '50.610-220':'Rua E',
}

#---CONSULTA DO USUÁRIO---
var1 = str(input('Digite o CEP: '))
try:
  print(cep[var1])
except:
  print('Cep não cadastrado')