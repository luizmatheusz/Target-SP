import pandas as pd # Biblioteca para analise de dados

estados = [] # Vetor de estados

# Funcao para adicionar um estado e seu faturamento no vetor de estados
def add_estado(nome, faturamento):
    estados.append({'nome': nome, 'faturamento': faturamento})

# Funcao para calcular a porcentagem de representação do faturamento de um estado em relação ao total
def perc_estado(df):
    total = df['faturamento'].sum()
    
    print("==== REPRESENTAÇÃO DO FATURAMENTO TOTAL MENSAL ====")
    for estado in df.itertuples(index=False):
        print(f"{estado.nome}: R$ {estado.faturamento} ({(100*estado.faturamento/total).round(2)}%)")

# Adiciona os estados e seus respectivos faturamentos
add_estado(nome='SP', faturamento=67836.43)
add_estado(nome='RJ', faturamento=36678.66)
add_estado(nome='MG', faturamento=29229.88)
add_estado(nome='ES', faturamento=27165.48)
add_estado(nome='Outros', faturamento=19849.53)

# Calcula a porcentagem de representação de cada estado e mostra para o usuario
df_estados = pd.DataFrame(estados)
perc_estado(df_estados)