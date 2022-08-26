from crypt import methods
from json import JSONEncoder
import numbers
import string
from unittest import result
from flask import Flask, render_template, request , jsonify
from py_expression_eval import Parser



app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200 

@app.route("/")

def hello_world():

    return "<p>Olá Mundo!</p>"

@app.route('/teti_rangel')

def teti_rangel():
    return render_template('teti_rangel.html', ip = request.remote_addr)
        


@app.route('/lerForm', methods = ['GET','POST'])

def lerForm():
    if request.method == 'GET':
        return render_template('lerForm.html')
        
    if request.method =='POST':
       nome = request.form.get('nome')
       return render_template('lerForm.html', nome = nome)  

@app.route('/lista')

def lista():
    listaNomes = ['pedro', 'kleber', 'vanessa']
    return render_template('lista.html', listaNomes = listaNomes)
    
@app.route('/unidadeCurricular')

def unidadeCurricular():
    
    return render_template('unidadeCurricular.html')

@app.route('/calculadora', methods = ['POST','GET'])

def calculadora():
    
    if request.method == 'GET':
        return render_template('calculadora.html')
    if request.method =='POST' :
        if request.form.get('action') == 'calcular':
            screenText = request.form.get('screenText')
            parser = Parser()
            expr = parser.parse(screenText)        
            print(expr.evaluate({}))
            results = {'resulted' : expr.evaluate({})}
            return  results
        if request.form.get('action') == 'convertToBin':
            screenText = request.form.get('screenText')
            parser = Parser()
            expr = parser.parse(screenText)            
            binary = format(expr.evaluate({}),'b')
            print(binary)
            return {'resulted' : binary}
            
#fim        
       
if __name__ == "__main__" :    
    app.run(debug= True)

#novaCalculadora
#conversão alpha numerico para binario
#flask run --host= 0.0.0.0.