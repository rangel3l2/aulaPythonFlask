from array import array
from ast import If
from colorsys import rgb_to_hsv
from crypt import methods
from json import JSONEncoder
from lib2to3.pgen2 import token
from lib2to3.pytree import convert
import numbers
import os
from sre_constants import SUCCESS
import string
from unittest import result
from xml.etree.ElementTree import tostring
from flask import Flask, render_template,redirect, request , jsonify
from py_expression_eval import Parser
from random import randint
from PIL import Image
import base64
import io
import cv2
import numpy as numpy
import json
from Usuario import Usuario
from Triangulo import Triangulo
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__) 
#mysql: // alex22:pass@host/nomeDB

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://alex22:Fg#6u2t5HpYT.DT@db4free.net:3306/tads_dw1'

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.webp']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['IMAGE_UPLOADS'] = '/home/rangel3l/Documents/tads/AlexTETI/aulaPythonFlask/venv/teti_Rangel/static/img-upload'



@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return {'ip': request.remote_addr}, 200 

@app.route("/")

def redirecionaLocalhost():

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

@app.route('/addFotoLista', methods = ['GET', 'POST'])
def addFotoLista(listaFile = [], listaFilename = []):
   
    if request.method == 'GET':
        listaFile = ''
        return render_template('addFotoLista.html')
        
    if request.method =='POST':         
        
        file = request.files['image']  
        print(file) 
        filename = file.filename.split('.') 
        if file.filename != '':
            image_string = base64.b64encode(file.read())
            image_string = image_string.decode('utf-8')
            listaFilename.append(filename[0])
            listaFile.append(image_string)
            
            return render_template('addFotoLista.html',listaFile = listaFile, listaFilename = listaFilename, zip=zip)
        return render_template('addFotoLista.html')

@app.route('/converterPixel', methods = ['GET', 'POST'])
def converterImagemPixel(numCols = 512, numRows = 512   ):
   
    if request.method == 'GET':
        listaFile = ''
        return render_template('addFotoLista.html',convertPixel = 'converterPixel')
        
    if request.method =='POST':        

            
        file = request.files['image']   
        filename = file.filename.split('.') 
        if file.filename != '':
            img = cv2.imdecode(numpy.frombuffer(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
            imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            listRGB = imgRBG.tolist()
            myArray = [[listRGB[i][j][k+1]for i in range(numCols)] for j in range(numRows)for k in range(1)]
            

            def rgb_to_hex(r,g,b):
                return ('{:X}{:X}{:X}').format(r,g,b)
                #print(f'rgb({myArray})')    

            return render_template('converterPixel.html')


@app.route('/apiteti', methods = ['POST', 'GET'])

def blabla():
    token =  'ABC'    
    if request.method =='GET':
        return  render_template('blabla.html')
    
    if request.method=='POST':
        
        tokenform = request.form.get('token')
        
     
    if tokenform == token:
        return render_template('blabla.html', msn =  'SUCCESS')
    return render_template('blabla.html', msn = 'FAILURE')

@app.route('/validarUsuario',methods = ['POST', 'GET'])
def validarUser():
    if request.method == 'GET':
        return render_template('validarUser.html')
    if request.method == 'POST':
        user = Usuario()        
        user.nome = request.form.get('nome')
        user.password = request.form.get('password')
        print(user.nome,user.password)
        validation = user.validate()
        if validation:
            return "validado com sucesso"
        return "usuario e senha incorreto"
    
@app.route('/triangulo',methods = ['POST', 'GET'])
def trianguloProperties():
    if request.method == 'GET':
        return render_template('triangulo.html')
    if request.method == 'POST':
       tri = Triangulo()
       tri.ladoA = int(request.form.get('ladoA'))
       tri.ladoB = int(request.form.get('ladoB'))
       tri.ladoC = int(request.form.get('ladoC'))
       
       perimetro = tri.getPerimetro()
       maiorLado = tri.getMaiorLado()
       area = tri.getArea()
       print(perimetro)
       return render_template('triangulo.html', perimetro = perimetro, area = area, maiorLado = maiorLado, ladoA = tri.ladoA, ladoB = tri.ladoB, ladoC = tri.ladoC)
    
@app.route('/carro',methods = ['POST', 'GET'])
def carroProperties():
    if request.method == 'GET':
        return render_template('carro.html')
    if request.method == 'POST':
            tri = Triangulo()
    
    
    return   '<h1>Ola mundo</h1>' + render_template('carro.html')  


 
db =SQLAlchemy(app)
    
@app.route('/curso', methods = ['GET', 'POST'])

def course():
    class curso(db.Model):
        __table_args__ = {'extend_existing': True}
        curso_id = db.Column(db.Integer, primary_key=True)
        curso_nome=db.Column(db.String(45))
        curso_descricao=db.Column(db.String(200))
        curso_carga_horaria=db.Column(db.Integer)
    
    if request.method == 'GET':       
        lista_de_cursos = []          
        lista_de_cursos = curso.query.all()
        print(f'listacurso{lista_de_cursos}')        
        return render_template('addNomeCurso.html', lista_de_cursos=lista_de_cursos)
    
    if request.method == 'POST':
        curso = curso(
        curso_nome = request.form.get('curso_nome'),      
        curso_descricao = request.form.get('curso_descricao'),
        curso_carga_horaria = request.form.get('curso_carga_horaria')
        )
      
        db.session.add(curso)
       
        try:
            db.session.commit()
            return render_template('addNomeCurso.html' ,lista_de_cursos = 'Enviado com sucesso')
        except:
            return render_template('addNomeCurso.html' ,lista_de_cursos = 'não foi possivel enviar dados')
            
        
               
     
    
               
    
    

 

          
            
#fim        
       
if __name__ == "__main__" :    
   app.run(debug= True) 

#novaCalculadora
#conversão alpha numerico para binario
#flask run --host= 0.0.0.0.