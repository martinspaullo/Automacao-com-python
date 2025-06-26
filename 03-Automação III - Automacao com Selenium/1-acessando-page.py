from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1 - Utilizando o WebDriver
browser = webdriver.Firefox()

browser.get('http://www.amazon.com.br') # Retorna a pagina em si

# 2 - Acessando elementos numa página
elem = browser.find_element(By.ID, 'twotabsearchtextbox') # Pega o campo de busca
elem.send_keys('ps5') # Digita 'ps5' no campo de busca
elem.send_keys(Keys.ENTER) #pressiona enter para pesquisar
