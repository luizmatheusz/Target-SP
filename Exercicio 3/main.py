import json          # Biblioteca json 
import pandas as pd  # Biblioteca Pandas para analise dos dados

# Funcao para abrir o json
def open_json(path):
    try:
        with open(path, 'r') as arquivo:
            dados = json.load(arquivo)
            
        return dados
    except:
        print("Erro.")
        return []
    
# Funcao para calcular o menor faturamento (dia e valor)
def min_faturamento(df):
    df = df[df['valor'] > 0]
    id_min = df['valor'].idxmin()
    min = df.loc[id_min]
    dia_min = int(min['dia'])
    valor_min = min['valor']
    
    print("\n===== MENOR FATURAMENTO =====")
    print(f"Dia {dia_min} - $ {valor_min}")
    
# Funcao para calcular o maior faturamento (dia e valor)
def max_faturamento(df):
    df = df[df['valor'] > 0]
    id_max = df['valor'].idxmax()
    max = df.loc[id_max]
    dia_max = int(max['dia'])
    valor_max = max['valor']
    
    print("\n===== MAIOR FATURAMENTO =====")
    print(f"Dia {dia_max} - $ {valor_max}")
    
# Funcao para calcular a media de faturamento mensal, e em quantos dias o faturamento diario foi maior que esse
def faturamento_greater_avg(df):
    df = df[df['valor'] > 0]
    media_valor = df['valor'].mean()
    count_valor_greater_avg = df[df['valor'] > media_valor]['valor'].count()
    
    print("\n===== FATURAMENTO MENSAL =====")
    print(f"Faturamento médio mensal: $ {media_valor}")
    print(f"O faturamento diário foi maior que a média mensal em {count_valor_greater_avg} dias.\n")

path = "dados.json"          # Define o caminho do json dos dados
dados = open_json(path)      # Abre o arquivo e atribui a ele uma variavel
df = pd.DataFrame(dados)     # Transforma o arquivo em um DataFrame do Pandas
min_faturamento(df)          # Calculo do menor faturamento
max_faturamento(df)          # Calculo do maior faturamento
faturamento_greater_avg(df)  # Calculo do faturamento mensal