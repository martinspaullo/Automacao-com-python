from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Acessando o site
browser = webdriver.Firefox()
browser.get('https://registro.br')

# 2 - Buscando elementos
elem = browser.find_element(By.ID, 'is-avail-field')  # Busca elemento pelo id
elem.clear() # limpa caso tenha algo digitado
elem.send_keys('botscompython.com.br') # Digita campo no elemento de busca
elem.send_keys(Keys.ENTER) # Clica enter
time.sleep(5) # Adiciona um tempo de espera
browser.save_screenshot('dominio.png') # Tira uma print da tela


# 3 - Buscando informações
results = browser.find_elements(By.TAG_NAME, 'strong')
# import pdb  # Modulo nativo para teste
# pdb.set_trace() # Abre o pdb no terminal
print(f'Domínio {results[1].text} está {results[2].text}') #Concatena os dois resultado e mostra no terminal
print(f'Preço anual: {results[3].text} \nPreço 2 anos: {results[4].text}') 
# browser.quit()  # Fecha o navegador