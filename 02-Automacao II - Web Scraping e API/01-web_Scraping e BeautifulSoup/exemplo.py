import requests

# 1 - Versão e metodos da biblioteca
# print(requests.__version__)

# 2 - Realizando requisição GET
link = 'https://www.google.com/search?q=futebol'

requisicao = requests.get(link)
print(requisicao)
print(requisicao.status_code)
# print(requisicao.text)