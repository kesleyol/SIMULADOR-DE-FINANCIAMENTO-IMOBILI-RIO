#AUTOR: KESLEYOL
#Programa para captar dados de possíveis investidores
from math import log

nome = str(input('Olá! Qual é o seu nome completo?')).title()
idade = int(input('Qual a sua idade?'))
profissao = str(input('Qual a sua profissão?')).title()
salario_bruto = float(input('Qual o seu salário bruto?'))
salario_liquido = float(input('Qual o seu salário líquido?'))
objetivo = str(input('Qual o seu objetivo investindo?'))
aporte_mensal = float(input('Qual o valor do aporte mensal que você planeja fazer?'))
taxa_juros = float(input('Qual taxa de juros anual deseja usar?'))
meta = float(input('Qual sua meta de patrimônio?'))
idade_meta = int(input('Com que idade você pretende atingir essa meta?'))

meses = (idade_meta - idade)*12
juros = (taxa_juros/100)/12
patrimonio_final = aporte_mensal*(((1+juros)**meses-1)/juros)
diferenca_patrimonio = meta - patrimonio_final
renda_mensal = meta*juros
renda_mensal_real = patrimonio_final*juros
n_meses = log(1+(meta*juros/aporte_mensal))/log(1+juros)
anos = int(n_meses / 12)

if patrimonio_final >= meta:
    status = f"Parabéns! Com esses aportes você vai ultrapassar sua meta em R${abs(diferenca_patrimonio):.2f}!"
else:
    status = f"Ainda faltarão R${diferenca_patrimonio:.2f} para atingir seu objetivo."

print(f'''
Olá, {nome}! Você como {profissao} e com {idade} anos, recebe R${salario_bruto:.2f} bruto por mes e R${salario_liquido:.2f} líquido
Com {idade_meta} anos e um aporte mensal de r${aporte_mensal:.2F}
, você atingira seu objetivo em {anos} anos, e com {idade_meta} anos você tera um patrimônio de R${patrimonio_final:.2f}!
{status}
com seu objetivo de {objetivo} com R${meta:.2f} você terá uma renda mensal de R${renda_mensal:.2f}
com base no seu aporte e taxa de juros sua renda real será de R${renda_mensal_real:.2f}!''')
