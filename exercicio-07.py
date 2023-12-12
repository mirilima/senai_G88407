#import pandas as PD
#dados ={
   #"cidade":[ "camaçari","são paulo","santo andré", "são caetano do sul"]
  # }
#df = PD.DataFrame(dados)
#for dado in df.values:
   #  print(dado[0],dado[1])

import pandas as PD
dados_produtos = {
    'Produto': ['Camiseta', 'Saia', 'Sapato', 'Camiseta', 'Sapato'],
    'Vendas': [50, 35, 45, 70, 60],
    'Mês': ['Janeiro', 'Janeiro', 'Fevereiro', 'Janeiro', 'Fevereiro']
}
#DATAFRAME -> é uma maneira de rerpresentar e trabalhar dados como tabuliares,
# pode ser visto como tabela que organiza os dados em linhas e colunas criando uma estrutura bidimencional

df = PD.DataFrame(dados_produtos)

# produto mais vendido no mes Janeiro #
produto_mais_vendido_janeiro = df[df['Mês'] == 'Janeiro']['Produto'].value_counts().idxmax()

#IDXMAX-> retorna o indice da primeira ocorrencia do maximo sobre o eixo do solicitado 

# value_count -> para contar o numero de ocorrencias de cada produto em todo DATAFRAME
 
# aumento percentual de camisetas de Janeiro pra Fevereiro #
vendas_camisetas_janeiro = df[(df['Produto'] == 'Camiseta') & (df['Mês'] == 'Janeiro')]['Vendas'].sum()
vendas_camisetas_fevereiro = df[(df['Produto'] == 'Camiseta') & (df['Mês'] == 'Fevereiro')]['Vendas'].sum()
aumento_percentual_camisetas = ((vendas_camisetas_fevereiro - vendas_camisetas_janeiro) / vendas_camisetas_janeiro) * 100


# produto mais vendido no geral #
produto_mais_vendido_geral = df['Produto'].value_counts().idxmax()
print("Produto mais vendido em Janeiro foi:", produto_mais_vendido_janeiro)
print("Aumento percentual nas vendas de camisetas de Janeiro para Fevereiro é de:", aumento_percentual_camisetas, "%.")
print("Produto mais vendido no geral foi:", produto_mais_vendido_geral)