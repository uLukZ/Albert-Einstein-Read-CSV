import pandas as pd   

''' Variavel com o caminho da planilha''' 
caminho_planilha = 'Faturamento.csv'  

''' Leitura da planilha CSV'''
leitor_linhas = pd.read_csv(caminho_planilha)

''' Calcula o faturamento'''
leitor_linhas['Faturamento'] = leitor_linhas['Quantidade'] * leitor_linhas['Preco_unitario']

''' Imprime o faturamento dos produtos'''
for index, row in leitor_linhas.iterrows():
    print(f"Produto: {row['Produto']}, Faturamento: {row['Faturamento']}")

''' Encontra os produtos com maior e menor faturamento'''
indice_maior_faturamento = leitor_linhas['Faturamento'].idxmax()
produto_maior_faturamento = leitor_linhas.loc[indice_maior_faturamento]

indice_menor_faturamento = leitor_linhas['Faturamento'].idxmin()
produto_menor_faturamento = leitor_linhas.loc[indice_menor_faturamento]

print("")

''' Imprime os produtos com maior e menor faturamento'''
print(f"Produto com maior faturamento: {produto_maior_faturamento['Produto']}, R${produto_maior_faturamento['Faturamento']}")
print(f"Produto com menor faturamento: {produto_menor_faturamento['Produto']}, R${produto_menor_faturamento['Faturamento']}")