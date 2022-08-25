from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def hello_world():

    return "<p>unidade curricular!</p>"

@app.route('/aula17')  
def aula17():
     return render_template('aula17-08.html') 

@app.route('/lerForm', methods = ['POST'])
def lerForm():
    if request.method =='POST':
       nome = request.form.get('nome')
       return render_template('aula17-08.html', nome = nome)  

@app.route('/lista')
def lista():
    listaNomes = ['pedro', 'kleber', 'vanessa']
    return render_template('lista.html', listaNomes = listaNomes)
    
@app.route('/unidadeCurricular')       
def unidadeCurricular():
    numero = 30
    return render_template('unidadeCurricular.html')
@app.route('/conteudoAula')
def conteudoAula():
    return render_template('teti_Rangel.html')
        
@app.rout('/calculadora')
def calculadora():
    return render_template('calculadora.html')  

if __name__ == "__main__" :    
    app.run(debug= True)

#novaCalculadora
#conversão alpha numerico para binario
#flash run --host= 0.0.0.0.