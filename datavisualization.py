import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.3/ratings.csv"
df = pd.read_csv(uri)
df.columns = ["UsuarioId", "filme", "nota", "DataDeEnvio"]
usuarios = df['UsuarioId']
notas = df['nota']
media = notas.mean()
#histograma = notas.hist() #grafico histograma, não da pra ver pelo vscode sem o plt.show

palette = sns.color_palette("Blues", 10) # "Blues"= nome da palete de cores, 10 = numero de cores que precisa 
sns.countplot(notas, palette=palette)
plt.title('Notas')
plt.show()

sns.distplot(notas)
#esse grafico é só de exemplo (esta errado)
plt.show()