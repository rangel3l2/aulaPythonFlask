from crypt import methods
from json import JSONEncoder
from unittest import result
from flask import Flask, render_template, request
from py_expression_eval import Parser
 
app = Flask(__name__)

@app.route("/")

def hello_world():

    return "<p>unidade curricular!</p>"


@app.route('/writeForm', methods = ['GET','POST'])
def lerForm():
    if request.method == 'GET':
        return render_template('aula17-08.html')
        
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
        

@app.route('/calculadora', methods = ['POST','GET'])

def calculadora():
    if request.method == 'GET':
        return render_template('calculadora.html')
    if request.method =='POST':
        screenText = request.form.get('screenText')
        parser = Parser()
        expr = parser.parse(screenText)        
        print(expr.evaluate({}))
        results = {'resulted' : expr.evaluate({})}
        return  results
        

if __name__ == "__main__" :    
    app.run(debug= True)

#novaCalculadora
#conversão alpha numerico para binario
#flask run --host= 0.0.0.0.