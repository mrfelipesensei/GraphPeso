import matplotlib.pyplot as plt
from datetime import datetime

#Dados fornecidos
datas = ['10/8/2024','12/8/2024','17/8/2024','27/8/2024']
pesos = [84.75, 85.25, 84.35, 84.54]

#Converter as datas para o formato datetime
datas = [datetime.strptime(data, '%d/%m/%Y') for data in datas]

#Criar o gráfico de linha
plt.figure(figsize=(10,6))
plt.plot(datas,pesos, marker='o', linestyle='-', color='red')

#Configurar o formato das datas para exibir apenas dia e mês
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m'))

#Configurar o gráfico
plt.title('Variação de Peso em Agosto de 2024')
plt.xlabel('Data')
plt.ylabel('Peso (kg)')
plt.grid(True)

#Exibir o gráfico
plt.show()