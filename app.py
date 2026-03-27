from flask import Flask, render_template, request #Flask é reponsável por conectar o app.py com o html

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    temp = None #Inicialização das variáveis
    fahre = None
    erro= None

    if request.method == 'POST': #apenas irá rodar a lógica abaixo ao apertar o botão na página, sem esse if irá ficar executando ao abrir a página
        try:
            #Receber os dados
            temp = float(request.form['temp'])
    
            #logica do exercicio
            fahre = (temp * 1.8) + 32
            
        except ValueError:
            erro = "Informação inválida, digite números válidos"
        except Exception as erro2: #caso erro sem ser erro no valor será usado Exception
            erro = (f"Erro inesperado", {erro2}) #trás o erro do navegador
            
    return render_template('index.html', temp=temp, fahre=fahre, erro=erro)

if __name__ == '__main__': #para não ter que fica digitando flask run no terminal
    app.run(debug=True, port=5000)