from openpyxl import Workbook

#1 - Criando Workbook
wb = Workbook() #workbook é responsavel por criar uma planilha
name = "file/test.xlsx"

#2 - Criando Worksheet
ws1 = wb.active #Ativa a planilha criado anteriormente
ws1.title = "Planilha 1" #nomeia a planilha 

# Adicionando dados na planilha
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2023, '25%', '45%'],
    [2023, '45%', '55%'],
    [2023, '70%', '40%'],   
]

"""
Portanto, esse for pega todas as linhas da variável data e insere essas linhas uma por uma na 
planilha ws1. A função append é usada para adicionar os dados nas células da planilha, automaticamente
preenchendo as colunas de acordo com o número de elementos em cada linha.Em resumo, o for é responsável
por adicionar as linhas de dados na planilha ws1.
"""
for line in data: # 
    ws1.append(line)
    
ws2 = wb.create_sheet(title="Pi") #Criando planilha 2 "PI"
ws2['D2'] = 3.14  #Inserindo dados na coluna "D2"
    
wb.save(filename=name) 