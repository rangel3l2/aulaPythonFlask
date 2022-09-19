const container = document.querySelector('#container')

const createCalc = (()=>{
    const screen = document.createElement('div')
    screen.id = `screen`   
    const calculator = document.createElement('div')
    calculator.id = 'calculator'
    const divButtonController = document.createElement('div')
    divButtonController.id = 'divButtonController'   
    const calculatorNumbers = document.createElement('div')
    calculatorNumbers.id = `calculatorNumbers`   
    container.appendChild(calculator)
      //tela calc
    calculator.appendChild(screen)
    //botão liga desliga
    calculator.appendChild(divButtonController) 
       
    // div calc numbers
    calculator.appendChild(calculatorNumbers)   
     //div Button Operation
    const divButtonOperation = document.createElement('div')    
    divButtonOperation.id = `divButtonOperation`
    calculator.appendChild(divButtonOperation)
    const screenText = document.createElement('h1')
    screen.appendChild(screenText)
    screenText.id='screenText'
   
    for (let i = 0; i <=1; i++) {
        const buttonController = document.createElement('button')
        buttonController.id = `buttonOperation`
        divButtonController.appendChild(buttonController)
        if(i==1){buttonController.innerHTML = `<h5>START</h5>`
        buttonController.addEventListener('click',()=>{screenText.innerText = 0})}
        if(i==0){buttonController.innerHTML = `<h5>BACK</h5>`
        buttonController.addEventListener('click',()=>{screenText.innerText = screenText.innerText.substring(0, screenText.innerText.length - 1)})
    }
    }
      
    const length = 11
    //operadores
    for (let i = 0; i <=4; i++) {
        const buttonOperation = document.createElement('button')
        buttonOperation.id = `buttonOperation`
        divButtonOperation.appendChild(buttonOperation)
        if(i==0)buttonOperation.innerHTML = `<h1>+</h1>`
        if(i==1)buttonOperation.innerHTML = `<h1>-</h1>`
        if(i==2)buttonOperation.innerHTML = `<h1>*</h1>`
        if(i==3)buttonOperation.innerHTML = `<h1>%</h1>`
        if(i==4){
            buttonOperation.innerHTML = `<h1>=</h1>`
            buttonOperation.addEventListener('click',()=>{
              //  console.log(screenText.innerText)
              
                $.ajax({
                    type: "POST",
                    url: '/calculadora',
                    datatype : JSON,
                    data: {
                        screenText : screenText.innerText,
                        action : 'calcular'
                    },
                    success : function(response){
            
                      //  console.log(`response${response.success}`)
                        screenText.innerText = response.resulted
                        
                    },
                    error: ((response)=>{
                        console.log(`response${response}`)

                    })
                    
                                      
                    
                  });
                  
                  
                // const formEnviar = document.createElement('form')
                // formEnviar.setAttribute('method','POST')
                // formEnviar.setAttribute('action','/lerCalculo')
                // const inputForm = document.createElement('button')
                // formEnviar.appendChild(inputForm)
                
                // formEnviar.appendChild(buttonOperation)
                // .setAttribute('type','hidden')
                // inputForm.setAttribute('name','equal')
                // inputForm.setAttribute('value',screenText)
                // container.appendChild(formEnviar)


                // buttonOperation.setAttribute('type','submit')
                
            })
        }
        if(i!==4){
        buttonOperation.addEventListener('click',()=>{
            
            screenText.innerText+=buttonOperation.innerText
        })
    }
    }
    
    
    //button
    for(i=0;i<=length;i++){
        const buttonNumber = document.createElement('button')
        buttonNumber.id = `id${i}`
        buttonNumber.className = `button`
        calculatorNumbers.appendChild(buttonNumber)
        if(i<=9){
       
        buttonNumber.innerHTML=`<h1>${length-2-i}</h1>`
        
        }
        if(i==10)buttonNumber.innerHTML=`<h1>.</h1>`
        if(i==11){
            buttonNumber.innerHTML=`<h1>Conv Biná</h1>`
            let cont  = 0
            buttonNumber.addEventListener('click',()=>{
                cont ++
                if(cont%2 ==0){ buttonNumber.innerHTML=`<h1>Conv Biná</h1>`
            }else{buttonNumber.innerHTML=`<h1>Conv Real</h1>`}
               
                
                
                $.ajax({
                    type: "POST",
                    url: '/calculadora',
                    datatype : JSON,
                    data: {
                        screenText : screenText.innerText,
                        action : 'convertToBin',
                        cont : cont
                        
                    },
                    success : function(response){
                        
                      //  console.log(`response${response.success}`)
                     
                            screenText.innerText = response.resulted 
                           
                      
                        
                    },
                    error: ((response)=>{
                        console.log(`response${response}`)
    
                    })
                    
                                      
                    
                  });
            })
            
        } 
    if(i<11){

           
         buttonNumber.addEventListener('click',()=>{
            if(screenText.innerText==0)screenText.innerText = '' 
            screenText.innerText +=`${buttonNumber.innerText}` 
        })
        buttonNumber.addEventListener('keypress',(event)=>{
            if(screenText.innerText==0)screenText.innerText = ''
            if(event.key){

                screenText.innerText += `${event.key}`    
            }
        })
    }
        
    
    }

   
    

})
createCalc()