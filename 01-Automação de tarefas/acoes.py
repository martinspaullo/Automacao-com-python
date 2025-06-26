import yfinance as yf  #biblioteca de financas do yahoo
from datetime import datetime
from matplotlib import pyplot as plt #Biblioteca usada para gerar grafico

end_data = datetime.now().strftime('%Y-%m-%d') #Pega a data atual
print(end_data)
bb = yf.Ticker('BBAS3.SA') #pega o ticker de sua preferencia
data_bb = bb.history(
        #"BBAS3.SA", 
        start="2020-07-16", #data de inicio
        end=end_data, 
)
data_bb['Close'].plot() #Preco de fechamento
plt.savefig('bb_preco.png') #salva arquivo "bb_preco.png"
print(data_bb.tail())
data_bb['Volume'].plot() #pega volume
plt.savefig('bb_volume.png') #salva arquivo "bb_preco.png"