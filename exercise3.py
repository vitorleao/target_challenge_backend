import json

def calcular_faturamento(faturamento_data):
    # Extrair os valores de faturamento ignorando os dias sem faturamento
    faturamento_dias = [item['valor'] for item in faturamento_data if item['valor'] > 0]
    
    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_dias)
    maior_faturamento = max(faturamento_dias)
    
    # Calcular a média mensal (excluindo os dias sem faturamento)
    media_mensal = sum(faturamento_dias) / len(faturamento_dias)
    
    # Calcular o número de dias com faturamento superior à média
    dias_superior_media = sum(1 for valor in faturamento_dias if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_superior_media

# Carregar os dados do faturamento a partir do arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

# Calcular os resultados
menor_faturamento, maior_faturamento, dias_superior_media = calcular_faturamento(data['faturamento'])

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média mensal: {dias_superior_media}")

