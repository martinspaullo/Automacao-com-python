from pathlib import Path
from datetime import datetime

root_dir = Path('file')

for path in root_dir.glob('**/*'):
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_birthtime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
        #print(date_created_str) #mostra a data e hora formatada
        new_filename = f'{date_created_str}-{path.name}' #pega a data e hora formatada e junta com o nome do arquivo
        new_filepath = path.with_name(new_filename) 
        path.rename(new_filepath) #renomeia o arquivo