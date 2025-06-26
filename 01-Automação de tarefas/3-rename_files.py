from pathlib import Path

root_dir = Path('file') #Caminho, pasta principal
# file_paths = root_dir.iterdir() #iterdir e usado para interar os valores e saber o que tem neles
# for path in file_paths:
#     #print(path)
#     for filepath in path.iterdir():
#         print(filepath)
file_paths = root_dir.glob("**/*") #Faz leitura automatica de todos os valores
for path in file_paths:
    if path.is_file(): # se tiver arquivos 
        #print(path)
        # parent_folder = path.parts
        # print(parent_folder)
        # print(parent_folder[-2]) # mostra a subpasta
        parent_folder = path.parts[-2] #pega a subpasta
        new_filename = f'{parent_folder}-{path.name}'
        print(new_filename)
        new_filepath = path.with_name(new_filename) #pega o novo nome de pasta 
        path.rename(new_filepath) #Renomeia os nomes dos arquivos