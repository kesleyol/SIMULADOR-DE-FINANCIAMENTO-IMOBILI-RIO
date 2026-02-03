#AUTOR KESLEYOL
#PROGRAMA PENSADO PARA MOTORISTAS DE APLICATIVO


quilometros = float(input('Quantos km você rodou hoje?'))
media = float(input('Qual a média do carro no painel?'))
valor_litro = float(input('Quanto você está pagando por litro?'))
faturamento = float(input('Quanto você faturou hoje?'))

#CALCULO DO CUSTO DO MOTORISTA
litros = quilometros / media
custo_combustivel = litros * valor_litro
custo_por_km = custo_combustivel / quilometros

#VALOR LÍQUIDO POR  DIA E KM
valor_liquido_dia = faturamento - custo_combustivel
valor_liquido_km = valor_liquido_dia / quilometros

#RESULTADO DO PROGRAMA
print(f'''
Custo com combustível por km hoje: R${custo_por_km:.2f}.
Custo com combustível total hoje: R${custo_combustivel:.2f}.
Faturamento líquido: R${valor_liquido_dia:.2f}.
Faturamento líquido por km: R${valor_liquido_km:.2f}.
Outros custos devem ser computados.''')
