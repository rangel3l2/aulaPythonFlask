const container = document.querySelector('#container')

const createCalc = (()=>{
    const screen = document.createElement('div')
    screen.id = `screen`   
    const calculator = document.createElement('div')
    calculator.id = 'calculator'
    const calculatorNumbers = document.createElement('div')
    calculatorNumbers.id = `calculatorNumbers`   
    container.appendChild(calculator)
      //tela calc
    calculator.appendChild(screen)
    // div calc numbers
    calculator.appendChild(calculatorNumbers)   
     //div Button Operation
    const divButtonOperation = document.createElement('div')    
    divButtonOperation.id = `divButtonOperation`
    calculator.appendChild(divButtonOperation)
    const screenText = document.createElement('h1')
    screen.appendChild(screenText)
    screenText.id='screenText'
      
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
                        screenText : screenText.innerText
                    },
                    success : function(response){
                        response?console.log(response.resulted):response.data = 0
                      //  console.log(`response${response.success}`)
                        screenText.innerText = response.resulted
                        
                    },
                    error: ((response)=>{
                        console.log(`response${response}`)

                    })
                    
                                      
                    
                  });
                  const resultedCal = document.querySelector('#resulted')
                 
                  console.log(resultedCal.innerText)
                  screenText.innerText = resultedCal.innerText
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
        if(i==11)buttonNumber.innerHTML=`<h1>Conv Biná</h1>`       
         buttonNumber.addEventListener('click',()=>{
            
            screenText.innerText +=`${buttonNumber.innerText}` 
        })
        buttonNumber.addEventListener('keypress',(event)=>{
            
            if(event.key){
                
                screenText.innerText += `${event.key}`    
            }
        })
        
        
    
    }

   
    

})
createCalc()