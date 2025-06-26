from goose3 import Goose
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

# nltk.download('stopwords')

# 1 - Importando Artigo da Internet
g = Goose()
# url = '<https://blog.geekhunter.com.br/pretensao-salarial-disparidade-generos/>'
url = 'https://olhardigital.com.br/2023/08/08/seguranca/google-chrome-vai-atualizar-sistema-mais-vezes-para-evitar-brechas-de-seguranca/'
artigo = g.extract(url)
print(artigo.publish_date)
print(artigo.title)
print(artigo.meta_description)
print(artigo.links)
print(artigo.cleaned_text)

# 2 - Aplicando Análise Textual I
word_tokens = word_tokenize(artigo.cleaned_text)
print(word_tokens)
print(len(word_tokens))

portuguese_stops = set(stopwords.words('portuguese'))

# for palavra in word_tokens:
#     if palavra.lower() not in portuguese_stops:
#         print(palavra)
#         print(len(palavra))
palavras = [palavra for palavra in word_tokens if palavra.lower() not in portuguese_stops]
print(palavras)
print(len(palavras))

# 3 - Aplicando Análise Textual II
fdist = FreqDist(palavras)
# print(fdist.most_common(10))

novas_palavras = [palavra for palavra in palavras if palavra.isalnum()]
fdist = FreqDist(novas_palavras)
print(fdist.most_common(10))

def plot_cloud(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color = 'navy',
    colormap = 'rainbow',
    collocations = False,
    stopwords = STOPWORDS
).generate(" ".join(novas_palavras))

plot_cloud(wordcloud)
