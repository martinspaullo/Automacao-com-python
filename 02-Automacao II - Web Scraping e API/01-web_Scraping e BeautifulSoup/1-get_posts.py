# 1 - Conhecendo a API
# <https://jsonplaceholder.typicode.com/posts>

# 2 - Lendo dados com Get
import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

#Requesição GET
response = requests.get(url)

print(response.status_code)

# Print the response (Pegar os dados)
response_json = response.json()
print(response_json)
