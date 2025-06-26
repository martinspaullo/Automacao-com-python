import requests

# 1 - Mapeando Informações
headers = {'X-GitHub-Api-Version': '2022-11-28'} #Sentando uma versão especifica!

base_api = 'https://api.github.com'
owner = 'OneBitCodeBlog'
url = f'{base_api}/users/{owner}/repos' #Montando a url

#Realizando a requisição
response = requests.get(url, headers=headers) 

# 2 - Conferindo o Resultado
print(response.status_code)
print(response.json())
print(len(response.json()))