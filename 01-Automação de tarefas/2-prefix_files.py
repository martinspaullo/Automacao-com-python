from pathlib import Path

root_dir = Path('dados')
file_paths = root_dir.iterdir()
#print(list(file_paths))
for file in file_paths:
    new_filename = f'new-{file.stem}{file.suffix}' #acrecente "new-" antes do nome do arquivo
    print(new_filename)
    #new_filepath = Path(new_filename)
    new_filepath = file.with_name(new_filename)
    file.rename(new_filepath) #renomeia o arquivo