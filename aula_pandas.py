import pandas as pd

pd.Series(data=5)

lista_nomes = 'Eudes Luzy Hallana Ná Ayla'.split()

pd.Series(lista_nomes)

dados = {
    'nome1': 'Eudes',
    'nome2': 'Luzy',
    'nome3': 'Hallana',
    'nome4': 'Ná',
    'nome5': 'Ayla',
}

pd.Series(dados)

print(dados)

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print('Quantidades de linhas = ', series_dados.shape) #etorna uma tupla com o numero de linhas
print('Tipo de dados = ', series_dados.dtypes) #Retorna o tipo de dados, se for misto será object
print('Os valores são únicos? = ', series_dados.is_unique) #Verifica se os valores são unicos (sem duplicações)
print('Existem valores nulos? = ', series_dados.hasnans) #RVerifica se existem valores nulos
print('Quantos valores existem? = ', series_dados.count()) #Conta quantos valores existem (exclui os nulos)

print('Qual o menor valor? = ', series_dados.min()) #Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor? = ', series_dados.max()) #Extrai o valor maximo com a mesma condição do minimo
print('Qual a média aritimetica? = ', series_dados.mean()) #Extrai a média aritimetica de uma Séries numérica
print('Qual o desvio padrão? = ', series_dados.std()) #Extrai o desvio padrão de uma Série numérica
print('Qual a mediana? = ', series_dados.median()) #Extrai a mediana de uma Séries numerica
print('\nResumo::\n', series_dados.describe()) #Conta quantos valores existem (exclui os nulos)

lista_nomes = 'Eudes Luzy Hallana Ná Ayla'.split()

lista_nomes = pd.DataFrame(lista_nomes, columns=['nome'])
print(lista_nomes)

url = 'https://pt.wikipedia.org/wiki/Minnesota'
dfs = pd.read_html(url)
print(type(dfs))
print(len(dfs))