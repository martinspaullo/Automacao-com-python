from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 1 - Utilizando o Webdriver

browser = webdriver.Firefox()
browser.get('https://registro.br') # Acessando o Browser

# 2 - Lista de Domínios

domains = [ # Lista de dominios
    'botscompython.com.br',
    'meta.com',
    'databot.com',
    'pythonbootcamp.com'
]

file = open('domains.txt', 'w', encoding='utf-8') # Cria um arquivo txt "domains.txt"

# 3 - Manipulando elementos
for domain in domains: # for para interar todos os itens da lista de dominios
    elem = browser.find_element(By.ID, 'is-avail-field') # # Busca elemento do browser pelo id (Campo de busca)
    elem.clear() # limpa
    elem.send_keys(domain) # pega item da lista de dominio e digita do campo de busca
    elem.send_keys(Keys.ENTER) # Clica enter
    time.sleep(5) # Tempo de espera
    
# 4 - Buscando Informações
    results = browser.find_elements(By.TAG_NAME, 'strong')  # Busca elemento do browser pelo name 
    text = f'Domínio {results[1].text} está {results[2].text}\n'
    print(text)
    file.write(text)

file.close()
browser.close()