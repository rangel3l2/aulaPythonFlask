from ast import If
from crypt import methods
from json import JSONEncoder
import numbers
import string
from unittest import result
from xml.etree.ElementTree import tostring
from flask import Flask, render_template, request , jsonify
from py_expression_eval import Parser
from random import randint
from flask import session


app = Flask(__name__) 


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return {'ip': request.remote_addr}, 200 

@app.route("/")

def redirect():

    return render_template('teti_rangel.html')

@app.route('/teti_rangel')

def teti_rangel():
    return render_template('teti_rangel.html', ip = request.remote_addr)
@app.route('/soma')   
def soma():
     if request.method == 'GET':
        soma = request.form.get
        print(soma)     
 

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
    



@app.route('/addNomeLista', methods = ['GET','POST'])

def addNomeLista(lista = []):
   
    if request.method == 'GET':
     
        return render_template('addNomeLista.html')
        
    if request.method =='POST': 
        nome = request.form.get('nome') 
        lista.append(nome)
        print(lista)
        return render_template('addNomeLista.html', listaNomes = lista)


          
@app.route('/addNomeDicionario', methods = ['GET','POST'])
def addNomeDicionario(user = [{}]):
    if request.method == 'GET':
        return render_template('addNomeDicionario.html')
        
    if request.method =='POST':
        nome = request.form.get('nome')
        nota = request.form.get('nota')
        KEYS = ['nome', 'nota']
        values = [nome, nota]
        user.append(dict(zip(KEYS, values)))
        return render_template('addNomeDicionario.html', user = user ) 

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
            cont = request.form.get('cont')
            intCont =  int(cont)
            if(intCont%2==0):
                binary= int(screenText, 2)    
                return {'resulted':binary}
              
            else:
                parser = Parser()
                expr = parser.parse(screenText)            
                binary = format(expr.evaluate({}),'b')
                return {'resulted' : binary,}

@app.route('/calculadoraAlfanumerica', methods = ['POST','GET'])

def calculadoraAlfanumerica(): 
    if request.method == 'GET':
        return render_template('calculadoraAlfanumerica.html')
    if request.method == 'POST':
        if request.form.get('action')=='converter':
            intCont =  int(request.form.get('cont'))
            if( intCont % 2 ==1):
                screenText = request.form.get('screenText')
                resulted =  ' '.join(format(ord(c), 'b') for c in screenText)                
                return jsonify({'resulted':resulted})
            else:
                screenText = request.form.get('screenText')
                resulted = ''.join(chr(int(screenText[i*8:i*8+8],2)) for i in range(len(screenText)//8))
                return jsonify({'resulted': resulted})

@app.route('/pixel', methods = ['GET', 'POST'])
def Pixel(numCols = 512, numRows = 512):
    if request.method == 'GET':
        return render_template('pixel.html')
    if request.method == 'POST':
        if(request.form.get('action') == 'randomColors'):
            myArray = [['#%06X' % randint(0, 0xFFFFFF) for i in range(numCols)] for j in range(numRows)]
            myArray.append('#%06X' % randint(0, 0xFFFFFF))
                       
          
            return {'resulted' : myArray}
listaFoto = []
@app.route('/addFotoLista', methods = ['GET', 'PUT'])
def addFotoLista():
   
    if request.method == 'GET':
     
        return render_template('addFotoLista.html')
        
    if request.method =='PUT': 
        nome = request.form.get('nome') 
        lista.append(nome)        
        return render_template('addFotoLista.html', listaFoto = listaFoto)



 

          
            
#fim        
       
if __name__ == "__main__" :    
   app.run(debug= True) 

#novaCalculadora
#conversão alpha numerico para binario
#flask run --host= 0.0.0.0.