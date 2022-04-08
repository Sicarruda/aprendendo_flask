from crypt import methods
from unittest import result
from flask import Flask, render_template, request

app = Flask(__name__)

# !!cria a primeira pagina!! 
# toda a pagina tem que ter:
# route -> link que vai ficar a pagina ex: http://meuSiteLindo.com/ORouteVemAqui
# função -> é o que eu quero exibir na pagina

@app.route('/')
def homepage():
	return render_template("homepage.html")


@app.route('/conta')
def faz_conta():
	return render_template('conta.html')


@app.route('/conta/<tipo_conta>', methods = ['POST', 'GET'])
def tipo_de_conta(tipo_conta):
	if request.method == 'POST':
		numero_1 = float(request.form['primeiro-numero'])
		numero_2 = float(request.form['segundo-numero'])
		resultado_conta = 0

		if tipo_conta == "div":
			resultado_conta = numero_1 / numero_2
			
	return render_template(f'{tipo_conta}.html', resultado = resultado_conta)

# !!coloca ela no ar!!
if __name__ == "__main__":
	app.run(debug=True)