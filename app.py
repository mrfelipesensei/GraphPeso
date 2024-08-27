from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib.dates as mddates
from datetime import datetime
import io
import base64


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        datas = request.form.get('datas').split(',')
        pesos = list(map(float, request.form.get('pesos').split(',')))

        #Converter as datas para o formato datetime
        datas = [datetime.strptime(data.strip(), '%d/%m/%Y') for data in datas]

        #Criar o gráfico de linha
        plt.figure(figsize=(10,6))
        plt.plot(datas,pesos,marker='o',linestyle='-',color='red')

        #Configurar o formato das datas para exibir somente dia e mês
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m'))

        #Configurar o gráfico
        plt.title('Variação de Peso em Agosto de 2024')
        plt.xlabel('Data')
        plt.ylabel('Peso (kg)')
        plt.grid(True)

        #Salvar o gráfico em um objeto bytes
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode('utf8')

        return render_template('result.html',img_data=img_base64)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)