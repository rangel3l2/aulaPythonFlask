const container = document.getElementById('container')
const calculadora = document.createElement('div')
calculadora.id = 'calculadora'
const NumberButton = 30
container.appendChild(calculadora)
const alpha = Array.from(Array(26)).map((e, i) => i + 65);
const alphabet = alpha.map((x) => String.fromCharCode(x));
const ArrayNumber = Array.from(Array(10).keys())
let suffleArray = null
createButton()
function createButton(){
     //tela calculadora
     const Tela = document.createElement('div')
     Tela.id = 'Tela'
     //controladores calculadora
     const controles = document.createElement('div')
     controles.id = 'controles'
     //botões gerais
     const botao = document.createElement('div')
     botao.id= 'botao'
    
    for (let i = 0; i < 5; i++){
       
        const buttonShufle = document.createElement('button')
        calculadora.appendChild(Tela)
        calculadora.appendChild(controles)
        calculadora.appendChild(botao)
        buttonShufle.id = `butaoControleid${i}`
        buttonShufle.className = `botaoControles`
        controles.appendChild(buttonShufle)
        if(i==0){
            
            buttonShufle.innerHTML=`<h2>123</h2>`
            buttonShufle.addEventListener('click',()=>{suffleArray =ArrayNumber
            
            createButtonGeneral()})
        }
        if(i==1){
            buttonShufle.innerHTML=`<h2>abc</h2>`
            buttonShufle.addEventListener('click',()=>{suffleArray = alphabet  
                           
            createButtonGeneral()})
        }
        if(i==2){

            buttonShufle.innerHTML=`<h2>ConvBin</h2>`
            buttonShufle.addEventListener('click',()=>{})
        }
        if(i==3){

            buttonShufle.innerHTML=`<h2>VOLTAR</h2>`
            buttonShufle.addEventListener('click',()=>{Tela.innerHTML = Tela.innerHTML.substring(0, Tela.innerHTML.length - 1)})
        }
        
        if(i==4){

            buttonShufle.innerHTML=`<h2>START</h2>`
            buttonShufle.addEventListener('click',()=>{})
        }
        
    }
    
  
}
//button general
   
function createButtonGeneral(){
    
    const botao = document.getElementById('botao')
    botao.innerHTML = ''
    for (let i = 0; i < suffleArray.length; i++) {
        const button = document.createElement('button')
        button.id = `buttonGeral${i}`
        button.className = 'botaoGerais'
        botao.appendChild(button)
        button.innerHTML = `<h2>${suffleArray[i]}</h2>`
    }
    writeOnScreen()
 } 
 function writeOnScreen(){
    const tela = document.getElementById('Tela')
    for (let i = 0; i < suffleArray.length; i++) {
        const button = document.getElementById(`buttonGeral${i}`)
        button.addEventListener('click',()=>{
            tela.innerHTML += button.innerText
            
        })
     sendData(tela)   
    }

 function sendData(tela){
    const converter = document.getElementById('butaoControleid2')
    let cont = 0
    converter.addEventListener('click',()=>{
        if(cont %2 == 1){
            converter.innerHTML = `<h2>convBin</h2>`
        }
        else
        {
            converter.innerHTML = `<h2>convText</h2>`
        }
       

        cont ++
    $.ajax({
        type: "POST",
        url: '/calculadoraAlfanumerica',
        datatype : JSON,
        data: {
            screenText : tela.innerHTML,
            action : 'converter',
            cont: cont
        },
        success : function(response){
            tela.innerHTML = response.resulted.toString()  
            console.log(`response${response.success}`)
            
            
        },
        error: ((response)=>{
            console.log(`response${response}`)

        })
        
                          
        
      });
      
    })
 }   
    


 }