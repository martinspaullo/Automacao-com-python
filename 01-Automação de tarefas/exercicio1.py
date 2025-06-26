import os

def organize_files(): # 
    types = ['exe', 'csv','jpg', 'pdf', 'zip', 'mp3', 'txt']

    # 1 - Diretório raiz 
    base_path = os.path.expanduser('~')
    # print(base_path)


    # 2 - Navega no diretório Downloads
    path = os.path.join(base_path, 'Downloads','teste') # os.path.join une um ou mais componentes.

    # print(path) 

    cwd = os.chdir(path) #fixa o diretorio

    # 3 - Lista arquivos do diretório
    list_files = os.listdir(cwd) #listdir pega o diretorio fixado e faz a listagem
    print(list_files)

    # 4 - Organizando arquivos
    for t in types: 
        if t not in os.listdir(): # verifica se ja existe a pasta
            os.mkdir(t) #cria a pasta
            
    for file in list_files:  #lista todos arquivos e pasta
        for t in types: #verifica o tipo de arquivo
            if '.' + t in file: # se tiver dentro file
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, t, file)
                os.replace(old_path, new_path) #move o arquivo para cada pasta correspondente

if __name__ == "__main__":
    organize_files()
