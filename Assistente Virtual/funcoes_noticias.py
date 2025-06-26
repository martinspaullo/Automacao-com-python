from requests import get 
from bs4 import BeautifulSoup

def ultima_noticias():
    url = 'https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419'
    site = get(url)
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:3]:
        titulo = item.title.text
        return titulo
