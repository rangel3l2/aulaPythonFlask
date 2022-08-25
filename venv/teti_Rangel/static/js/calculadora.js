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

    const length = 9
    //operadores
    for (let i = 0; i <=3; i++) {
        const buttonOperation = document.createElement('button')
        buttonOperation.id = `buttonOperation`
        divButtonOperation.appendChild(buttonOperation)
        if(i==0)buttonOperation.innerHTML = `<h1>+</h1>`
        if(i==0)buttonOperation.innerHTML = `<h1>-</h1>`
        if(i==1)buttonOperation.innerHTML = `<h1>*</h1>`
        if(i==2)buttonOperation.innerHTML = `<h1>%</h1>`
        if(i==3)buttonOperation.innerHTML = `<h1>=</h1>`

    }
    
    
    //button
    for(i=0;i<=length;i++){
        const buttonNumber = document.createElement('button')
        buttonNumber.id = `id${i}`
        buttonNumber.className = `button`
        buttonNumber.innerHTML=`<h1>${length-i}</h1>`
        calculatorNumbers.appendChild(buttonNumber)
    }

    
    

})
createCalc()