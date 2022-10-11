import pandas as pd

vendas_df = pd.read_excel("Projetos/vendas.xlsx")
#print(vendas_df.head(10)) #.head -> Exibe as 10 primeiras linhas

#print(vendas_df.shape) #.shape -> Mostra a quantidade de linhas e colunas

#print(vendas_df.describe()) #.describe -> Mostra algumas informações úteis

#print(vendas_df[['Data','Produto']]) #Pega a coluna ou uma Serie

#print(vendas_df.loc[1:5]) #.loc -> Pega uma linha ou um conjunto de linhas
#print(vendas_df.loc[vendas_df["Produto"]=="Relógio"])
#print(vendas_df.loc[vendas_df["Produto"]=="Relógio", ["Data", "ID Loja", "Quantidade"]])

'''Criando uma nova coluna'''
vendas_df['Comissão'] = vendas_df["Valor Final"]*0.05 #Se tiver a coluna Comissão, altera os valores, senão, cria uma nova coluna
#print(vendas_df)

'''Criando uma nova coluna com valor padrão'''
vendas_df.loc[:,"Imposto"] = 0 #Utilizar o .loc[linhas, colunas] para não bugar
#print (vendas_df)

'''Adicionando novas linhas a partir de outra tabela do excel'''
vendas_dez_df = pd.read_excel("Projetos/Vendas - Dez.xlsx")
vendas_df = pd.concat([vendas_df, vendas_dez_df]) #Utilizar o pd.concat([tabela1, tabela2])
#print(vendas_df)

'''Excluindo linhas e colunas'''
#vendas_df = vendas_df.drop("Imposto", axis=1) #axis -> 1 coluna / 0 linha
#vendas_df = vendas_df.drop(0, axis=0) #Exclui a linha 0
#print(vendas_df)

'''Deletando linhas e colunas que possuem valores vazios''' #USAR .dropna, prestar atenção no NA
#vendas_df = vendas_df.dropna(how= "all", axis=1) #Exclui qualquer coluna ou linha (verificar o axis) que tenha todos os valores NaN
#vendas_df = vendas_df.dropna() #Exclui as linhas que tenham valor NaN, toda a linha será excluída
#vendas_df = vendas_df.dropna(axis=1) #Exclui as colunas que tenham valor NaN, toda a coluna será excluída

'''Preenchendo os valores vazios (NaN) com algo'''
#vendas_df["Comissão"] = vendas_df["Comissão"].fillna(vendas_df["Comissão"]).mean() #Preenche com a média dos valores da mesma coluna
vendas_df = vendas_df.ffill() #Preenche com o último valor da tabela

'''Value Counts'''
#Calcula a quantidade de vezes que os itens se repetem em uma coluna
#transacoes_lojas=vendas_df["ID Loja"].value_counts()

'''Groupby'''
#Agrupa determinados itens de uma coluna com valores de outras colunas
#Por exemplo na tabela atual, qual é o faturamento por produto? Ou seja, quanto arrecadou cada produto?
#faturamento_produto=vendas_df.groupby('Produto').sum() #Agrupa todos os produtos e soma todas as outras tabelas numéricas
#faturamento_produto=vendas_df[["Produto", "Valor Final"]].groupby('Produto').sum() #Utiliza somente a coluna numérica de Valor Final

'''Mesclando 2 dataframes''' #.merge(dataframe que vai mesclar)
gerentes_df= pd.read_excel("Projetos/Gerentes.xlsx")
vendas_df = vendas_df.merge(gerentes_df) #Pega os gerentes do dataframe gerentes_df e adiciona a coluna ao vendas_df, por meio da relação dos shoppings

print(vendas_df)

'''Jupyter teste
import pandas as pd

vendas = pd.read_excel("Vendas.xlsx")
display(vendas.head(10))

Quantos produtos tem nas lojas
Qtd_vendas = vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum('Quantidade')
display(Qtd_vendas)

#Quantidade de cada produto em cada loja
qtd_vendas_produtos = vendas[['ID Loja', 'Produto', 'Quantidade']].groupby(['ID Loja', 'Produto']).sum('Quantidade')
display(qtd_vendas_produtos)'''