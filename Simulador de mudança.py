# Autor: Kesleyol
# Simulador de viabilidade financeira: Brasil vs Europa
#CONSIDERANDO UMA PESSOA CASADA COM FIHOS (PARA FINS DE CALCULO DE IMPOSTO)


sa = float(input('Qual o salário bruto na Alemanha?'))
ss = float(input('Qual o salário bruto na Suíça?'))
filhos = int(input('Quantos filhos você tem?'))
franco = float(input('Qual o valor do franco suíço hoje?'))
euro = float(input('Qual o valor do euro hoje?'))
anos = int(input('Por quantos anos você vai mandar dinheiro para o Brasil?'))
juros = float(input('Qual a taxa de juros anual?'))
meses = anos*12
juros_mensal = (juros/100)/12
salario_mensal_alemanha = sa/12
salario_mensal_suica = ss/12
impa = salario_mensal_alemanha * 0.63
imps = salario_mensal_suica * 0.78
ac = filhos * 250
mf = 15 * filhos
m2t = mf + 70
apartamento_alemanha = 14 * m2t
apartamento_suica = 25 * m2t
mercado_alemanha = 850.00
mercado_suica = 1400.00 
contas_alemanha = 350.00
contas_suica = 250.00
transporte_alemanha = 300.00
trasnporte_suica = 500.00
seguro_saude = (350*2)+(150*filhos)
custo_de_vida_alemanha = apartamento_alemanha+mercado_alemanha+contas_alemanha+transporte_alemanha
custo_de_vida_suica = apartamento_suica+mercado_suica+contas_suica+trasnporte_suica+seguro_saude
total_liquido_alemanha = impa+ac 
total_liquido_suica = imps+ac
envio_francos = (total_liquido_suica-custo_de_vida_suica) * franco
envio_euros = (total_liquido_alemanha-custo_de_vida_alemanha) * euro
ma = envio_euros*(((1+juros_mensal)**meses-1)/juros_mensal)
ms = envio_francos*(((1+juros_mensal)**meses-1)/juros_mensal)
impa = salario_mensal_alemanha * 0.63
imps = salario_mensal_suica * 0.78
total_liquido_alemanha = impa+ac 
total_liquido_suica = imps+ac

#CUSTO DE VIDA ALEMANHA

print(f'Com um salário bruto de {salario_mensal_alemanha} euros na Alemanha você vai receber líquido {impa}euros com um adicional de {ac} pelos filhos! dando um total de', total_liquido_alemanha,'!')
print(f'''Considerando os custos básicos na Alemanha:
Aluguel:{apartamento_alemanha} euros
Mercado:{mercado_alemanha} euros
Contas:{contas_alemanha} euros
Transporte:{transporte_alemanha} euros
da um total de''',custo_de_vida_alemanha,'''!
''')

#CUSTO DE VIDA SUÍÇA

print(f'Com um salário bruto de {ss} francos na Suíça, você vai receber líquido {imps}francos, com um adicional de {ac} pelhos filhos, ficando um total de', total_liquido_suica,'!')
print(f'''Considerando os custos básicos na Suíça:
Aluguel:{apartamento_suica} francos
Mercado:{mercado_suica} francos
Contas:{contas_suica} francos
Transporte:{trasnporte_suica} francos
Seguro súde: {seguro_saude} francos
da um total de''',custo_de_vida_suica,'!')

#SALÁRIO MENOS CUSTO DE VIDA


print(f'''Considerando o custo de vida e o salário líquido
Na Alemanha sobra: {total_liquido_alemanha-custo_de_vida_alemanha} euros
Na Suíça sobra: {total_liquido_suica-custo_de_vida_suica} francos''')

#INVESTIMENTO NO BRASIL


print(f'''Considerando a sobra e o valor das moedas hoje você enviaria para o Brasil:
Euros: R${envio_euros:.2f}
Francos: R${envio_francos:.2f}''')

#APOSENTADORIA

print(f'''
Investindo no brasilpor {anos}anos a uma taxa de {juros}% ao ano você teria:
Alemanha: R${ma:.2f}!
Suíça: R${ms:.2f}''')