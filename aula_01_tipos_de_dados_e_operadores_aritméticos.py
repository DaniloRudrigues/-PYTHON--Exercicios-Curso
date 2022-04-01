# -*- coding: utf-8 -*-
"""Aula 01 - [G] - Tipos de Dados e Operadores Aritméticos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/DaniloRudrigues/80ea15c16a347517837d87a1e2761cad/aula-01-g-tipos-de-dados-e-operadores-aritm-ticos.ipynb

# Exercícios

1. Faça um Programa que mostre a mensagem "Alo mundo" na tela
"""

print("Alô mundo")

"""
2. Faça um Programa que peça um número e então mostre a mensagem `O número informado foi [número]`."""

var = input("Digite um número: ")
print("O número informado foi",var)

"""
3. Faça um Programa que peça dois números e imprima a soma."""

var1 = float(input("Digite o primeiro número: "))
var2 = float(input("Digite o segundo número: "))
print("A soma dos dois números é:", var1 + var2)

"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

var1 = float(input("Digite a nota 1: "))
var2 = float(input("Digite a nota 2: "))
var3 = float(input("Digite a nota 3: "))
var4 = float(input("Digite a nota 4: "))
print("A média das notas é:", (var1 + var2 + var3 + var4)/4)

"""
5. Faça um Programa que converta metros para centímetros."""

var1 = float(input("Digite a quantidade de metros que deseja converter: "))
print("A quantidade de centímetros digitada é:", var1 * 100,"cm")

"""
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

import math
var1 = float(input("Digite o raio do círculo:"))
print("A área do círculo com a área digitada é:", math.pi*var1**2)

"""
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

var1 = float(input("Digite a tamanho dos lados de um quadrado em metros:"))
area_quad = var1**2
print("O dobro da área do quadrado escolhido é:",area_quad*2,"m²")

"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

var1 = float(input("Digite o quanto sua hora de trabalho (em R$/hora):"))
var2 = float(input("Digite a quantidade horas trabalhada no mês (em horas):"))
print("O salário que será recebido no referido mês é de: R$",var1*var2)

"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
$ °C = 5 \times ((°F-32) / 9) $"""

var1 = float(input("Digite a temperatura em Fahrenheit (°F):"))
cels = round(5 * ((var1 - 32) / 9),2)
print("A temperatura em Celsius é",cels,"°C")

"""10. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

$°F = (°C \times 9 / 5) + 32 $
"""

var1 = float(input("Digite a temperatura em Celsius (°C):"))
cels = round((var1*9/5)+32,2)
print("A temperatura em Fahrenheit é",cels,"°F")

"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    - o produto do dobro do primeiro com metade do segundo.
    - soma do triplo do primeiro com o terceiro.
    - terceiro elevado ao cubo."""

int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
rea1 = float(input("Por fim, digite um número real: "))

A = round(float(2*int1+int2/2),2)
B = round(float(3*int1+rea1),2)
C = round(rea1**3,2)

print("O produto do dobro do primeiro com metade do segundo é:",A)
print("A soma do triplo do primeiro com o terceiro é:",B)
print("O terceiro elevado ao cubo:",C)

"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:

$ peso\_ideal = (72.7 \times altura) - 58 $"""

var1 = float(input("Digite sua altura: "))
print("O peso ideal para sua altura de",var1, "é de:", round((72.7*var1)-58,2),"kg")

"""13. Tendo como dado de entrada a altura ($h$) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
- Para homens: $ (72.7 \times h) - 58 $
- Para mulheres: $ (62.1 \times h) - 44.7 $
"""

var1 = float(input("Digite sua altura: "))
i = str(input("Digite (m) para masculino ou (f) para feminino: "))

k=1
while k == 1:
  if i=='m':
    print("O peso ideal para sua altura de",var1, "e sexo masculino é de:", round((72.7*var1)-58,2),"kg")
    k=2
  elif i=='f':
    print("O peso ideal para sua altura de",var1, "e sexo feminino é de:", round((62.1*var1)-44.7,2),"kg")
    k=2
  else:
    print("Sexo digitado não cadastrado")
    i = str(input("Digite (m) para masculino ou (f) para feminino: "))

"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R\$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

peso = float(input('Digite o peso em kg dos pescados: '))

if peso >= 50.0:
  exc = float(peso - 50.0)
  multa = float(exc * 4)
  print('Houve excesso de peso de,',round(exc,2),'kg e há uma multa de, R$',round(multa,2))
else:
  print('NÃO Houve excesso de peso')

"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    - salário bruto.
    - quanto pagou ao INSS.
    - quanto pagou ao sindicato.
    - o salário líquido.
    - calcule os descontos e o salário líquido, conforme a tabela abaixo:

```
            + Salário Bruto : R$
            - IR (11%) : R$
            - INSS (8%) : R$
            - Sindicato ( 5%) : R$
            = Salário Liquido : R$
```
> Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

rph = float(input('Digite o quanto você ganha por hora (em R$/horas): '))
hor = float(input('Digite o número de horas trabalhadas no mês (em horas):'))

sal_bru = rph * hor
ir = 0.11*sal_bru
inss = 0.08*sal_bru
sind = 0.05*sal_bru
sal_liq = sal_bru - ir - inss - sind

print()
print('**********CONTRA-CHEQUE**********')
print('+   Salário Bruto: R$',sal_bru)
print('-        IR (11%): R$',ir)
print('-       INSS (8%): R$',inss)
print('-  Sindicato (5%): R$',sind)
print('= Salário líquido: R$',sal_liq)
print('*********************************')

"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs.: somente são vendidos um número inteiro de latas."""

import math

m2 = float(input('Digite a quantidade de área a ser pintada (em m²): '))

rend     = 1/3    # Rendimento de 1/3 l/m²
vol_lata = 18     # Litros por lata
prec     = 80.0   # preço de uma lata 

litros = m2 * rend
latas  = math.ceil(litros/vol_lata)
custo  = latas * prec

print('Serão necessárias',latas,'lata(s) resultando em R$',custo)

"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00 ou em galões de 3,6 litros, que custam R\$ 25,00.
  - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
  - comprar apenas latas de 18 litros;
  - comprar apenas galões de 3,6 litros;
  - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

m2 = float(input('Digite a quantidade de área a ser pintada (em m²): '))

rend     = 1/6    # Rendimento de 1/6 l/m²
# Latas
l_vol_lata = 18     # Litros por lata
l_prec     = 80.0   # preço de uma lata 
# Galões
g_vol_gal = 3.6     # Litros por galão
g_prec     = 25.0   # preço de uma galão

print('Serão apresentadas 3 situações de compras')
print()
print('************PRIMEIRA SITUAÇÃO************')
a = math.ceil(m2*rend/l_vol_lata)
b = l_prec*math.ceil(m2*rend/l_vol_lata)
print('Utilizando latas de',l_vol_lata,'litros. Serão necessárias',a,'latas com o preço total de R$',b)
print()
print('************SEGUNDA  SITUAÇÃO************')
c = math.ceil(m2*rend/g_vol_gal)
d = g_prec*math.ceil(m2*rend/g_vol_gal)
print('Utilizando galões de',g_vol_gal,'litros. Serão necessárias',c,'latas com o preço total de R$',d)
print()
print('************TERCEIRA SITUAÇÃO************')
if l_prec/l_vol_lata <= g_prec/g_vol_gal:
  resto = m2*rend % l_vol_lata
  e = m2*rend//l_vol_lata
  f = math.ceil(resto/g_vol_gal)
  t = l_prec*(m2*rend//l_vol_lata)+g_prec*(math.ceil(resto/g_vol_gal))
  print('Utilizando latas e galões. Serão necessárias',e,'latas e ',f,' galões com o preço total de R$',t)
else:
  restog = m2*rend % g_vol_gal
  x = m2*rend//g_vol_gal
  y = math.ceil(restog/l_vol_lata)
  tt = l_prec*y+g_prec*x
  print('Utilizando galões e latas. Serão necessárias',x,'galões e ',y,' latas com o preço total de R$',tt)

"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tarq = float(input('Digite o tamanho do arquivo (me MB): '))
vel = float(input('Digite a velocidade da internet (em Mbps): '))

seg = tarq / vel
min = seg / 60

print()
print('O tempo aproximado de download é',min,'minutos')