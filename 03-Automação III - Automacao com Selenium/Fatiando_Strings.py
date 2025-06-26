# Exemplo de fatiar string
frase = "Foram encontrado aproximadamente 12.000 peças" # String a ser fatiada

total = int((frase.split('aproximadamente')[1].split('peças')[0]).replace('.','')) # Fatiando a string
resultado = total / 2
print (f'Quantidade de peças: {resultado}') # Mostrando do resultado no terminal