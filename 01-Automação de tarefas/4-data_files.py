from pathlib import Path
from datetime import datetime

path = Path('file', 'dados', 'a.txt')
#print(path.stat()) # Mostra o Metadados (por meio do metadados e possivel mostrar o arquivo com data e hora)
stats = path.stat() # salva o valor stat metadados em uma string
second_created = stats.st_ctime #pega a informação da string stats
date_created = datetime.fromtimestamp(second_created) #pega os dados de data e hora
date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S') #formata para pegar somente a data e hora
print(stats)
print(second_created)
print(date_created)
print(date_created_str)
