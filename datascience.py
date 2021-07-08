import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.3/ratings.csv"
#data frame (notas de filmes)
DataFrame = pd.read_csv(uri)
print(DataFrame)

print(DataFrame.head(10)) # por default devolve as 5 primeiras linhas, pode se alterar o numero de linhas 
                         # colocando um valor dentro da função como o exemplo 10

print(DataFrame.columns) # mostra as colunas existentes
DataFrame.columns = ["usuarioid", "filmeid", "nota", "quandoenviou"] # alterando nome das colunas
print(DataFrame.columns)

Series = DataFrame["nota"] # apenas a coluna nota que foi renomeada
print(f'Notas: \n{Series.unique()}') # todas as notas existentes
print(f'Media: {Series.mean():.2f}') # media das notas, .min() nota minima, .max() nota maxima 

print(DataFrame.describe()) # Tabela com informaçoes uteis sobre o data frame
                          # Mediana = valor do meio que divide uma porcentagem 
                # exemplo: 50% (ganham menos que a mediana)  |Mediana|  (50% ganham mais que a mediana)

