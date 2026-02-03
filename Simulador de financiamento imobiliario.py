#AUTOR: Kesleyol
#SIMULADOR DE FINANCIAMENTO IMOBILIÁRIO 

valor_total = float(input('Qual o valor do imóvel?'))
entrada = float(input('Qual o valor da entrada?'))
ve = float(input('Quanto você espera pagar de parcela?'))
parcelas = int(input('Em quantas vezes vai ser parcelado o valor restante?'))

taxa_minima = (9/100) / 12
taxa_maxima = (12/100) / 12
anos = parcelas / 12
valor_financiado = valor_total - entrada
parcela9 =  valor_financiado * ((taxa_minima * (1 + taxa_minima)**parcelas) / ((1+taxa_minima)**parcelas-1))
parcela12 =  valor_financiado * ((taxa_maxima * (1 + taxa_maxima)**parcelas) / ((1+taxa_maxima)**parcelas-1))
porcentagem_entrada = (entrada / valor_total)*100
#VALOR FINAL TOTAL
vt_parcela9 = parcela9 * parcelas
vt_parcela12 = parcela12 * parcelas
diferenca_ve9 = parcela9 - ve
diferenca_ve12 = parcela12 - ve
vt_price9 = vt_parcela9 +  entrada
vt_price12 = vt_parcela12 + entrada


#COMPARAR TABELA SAC COM PRICE
amortizacao = valor_financiado / parcelas
juros_inicial9 = valor_financiado * taxa_minima
primeira_parcela9 = amortizacao + juros_inicial9
juros_inicial12 = valor_financiado * taxa_maxima
primeira_parcela12 = amortizacao + juros_inicial12
juros_final9 = amortizacao * taxa_maxima
parcela_final9 = amortizacao + juros_final9
juros_final12 = amortizacao * taxa_maxima
parcela_final12 = amortizacao + juros_final12
vt_sac9 = ((primeira_parcela9 + parcela_final9)/2) * parcelas + entrada
vt_sac12 = ((primeira_parcela12 + parcela_final12)/2) * parcelas + entrada


#LÓGICA PARA JUROS DE 9% A.A PRICE
if parcela9 <= ve:
    status9 = f'9% a.a está dentro do orçamento com uma sobra mensal de: R${abs(diferenca_ve9):.2f}!'
else:
    status9 = f'9% a.a ultrapassa o orçamento em: R${diferenca_ve9:.2f}!'

#LÓGIA PARA JUROS DE 12% A.A PRICE
if parcela12 <= ve:
    status12 = f'12% a.a está dentro do orçamento com uma sobra mensal de: R${abs(diferenca_ve12):.2f}!'
else:
    status12 = f'12% a.a ultrapassa o orçamento em: R${diferenca_ve12:.2f}!'

#LÓGIA COMPARAÇÃO ENTRE TABELAS 9% a.a
if vt_sac9 <= vt_price9:
    statussac9 = f'A tabela SAC é a mais vantajosa considerando o valor final, com uma difereça de R${abs(vt_price9-vt_sac9):.2f}!'
else:
    statussac9 = f'A tabela PRICE é a mais vantajosa considerando o valor final, com uma diferença de R${abs(vt_price9-vt_sac9):.2f}!'

#LÓGIA COMPARAÇÃO ENTRE TABELAS 12% a.a
if vt_sac12 <= vt_price12:
    statussac12 = f'A tabela SAC é a mais vantajosa considerando o valor final, com uma difereça de R${abs(vt_price12-vt_sac12):.2f}!'
else:
    statussac12 = f'A tabela PRICE é a mais vantajosa considerando o valor final, com uma diferença de R${abs(vt_price12-vt_sac12):.2f}!'


#TABELA PRICE
print(f'''
      TABELA PRICE:
Valor do imóvel: R${valor_total:.2f}.
Valor da entrada: R${entrada:.2f}.
Porcentagem entrada: {porcentagem_entrada:.2f}%!''')
print(f'Valor financiado: R${valor_financiado:.2f}.')
print(f'''
Valor final parcelas à 9% a.a: R${vt_parcela9:.2f}. 
Valor final parcelas à 12% a.a: R${vt_parcela12:.2f}.''')
print(f'''Parcela mensal 9% a.a: R${parcela9:.2f}.
Parcela mensal 12% a.a: R${parcela12:.2f}.''')
print(f'''Valor final 9% a.a: R${vt_price9:.2f}.
Valor final 12% a.a: R${vt_price12:.2f}.''')

print(f'{status9}')
print(f'{status12}')

#TABELA SAC
print(f'''
      TABELA SAC:
9% a.a:
Primeira parcela: R${primeira_parcela9:.2f}.
Última parcela: R${parcela_final9:.2f}.
12% a.a:
Primeira parcela: R${primeira_parcela12:.2f}.
Última parcela: R${parcela_final12:.2f}.
Valor final financiamento::
9%: R${vt_sac9:.2f}!
12%: R${vt_sac12:.2f}!''')

#COMPARAÇÃO ENTRE TABELAS DE FINANCIAMENTO IMOBILIÁRIO

print(f'{statussac9}')
print(f'{statussac12}')

