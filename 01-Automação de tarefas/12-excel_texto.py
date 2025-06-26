from openpyxl import Workbook

print("Lendo dados do arquivo de texto")

file_txt = open("files/gastos.txt", "r", encoding="utf-8") #Busca arquivo txt
file = file_txt.read() #faz a leitura do arquivo
# print(file)
list_data = file.splitlines() #divide o conteúdo lido do arquivo (file) em várias linhas, criando uma lista de strings.
# print(list_data)
for i in range(0, len(list_data)): #Este loop percorre todas as linhas de list_data
    list_data[i] = list_data[i].split(",") #para cada linha, usa o método split(",") para dividir a linha em elementos separados por vírgula.
# print(list_data)

wb = Workbook() # cria uma nova instância de uma planilha do Excel (um arquivo .xlsx
ws = wb.active # seleciona a planilha ativa onde os dados serão inseridos

for row in list_data: # Esse loop percorre cada sublista em list_data e adiciona esses dados como uma nova linha na planilha.
    ws.append(row) # é usada para adicionar a linha de dados à planilha.
    
wb.save('files/gastos.xlsx') #Salva