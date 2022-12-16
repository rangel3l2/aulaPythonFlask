const container = document.getElementById('container')
const width =10
const height = 10
const gameCanvas = document.createElement('div')
const squareArray = []
gameCanvas.id = 'gameCanvas'
container.appendChild(gameCanvas)
controllers()

function controllers(){
const divControllers = document.createElement('div')
divControllers.id = 'divControllers'
gameCanvas.appendChild(divControllers)
const buttonRight = document.createElement('button')
const buttonLeft = document.createElement('button')
const buttonShowMoves = document.createElement('button')
divControllers.appendChild(buttonRight)
divControllers.appendChild(buttonLeft)
divControllers.appendChild(buttonShowMoves)
buttonRight.id = 'buttonRight'
buttonLeft.id = 'buttonLeft'
buttonShowMoves.id = 'buttonShowMoves'
buttonRight.innerText = 'Direita'
buttonLeft.innerText = 'Esquerda'   
buttonShowMoves.innerText = 'Histórico'

} 
    createSquares()
function createSquares(){
    const squares = document.createElement('div')
    squares.id ='squares'
    gameCanvas.appendChild(squares)
    let j = 0
    for(let i = 0 ; i <height; i++){
        for(let j = 0 ; j <width; j++){
            const square = document.createElement('div')
      
             square.id = `id${i},${j}`
            squares.appendChild(square)
            square.classList.add('square')
            squareArray.push(square)
        }

    }

}

let RandomNumber = Math.floor(Math.random()*10) 
let randomNumber2 = Math.floor(Math.random()*10)
car()
function car(){
    
    const square = document.getElementById(`id${RandomNumber},${randomNumber2}`)
    const car = document.createElement('div')
    car.id = 'car'
    const carImagem = document.createElement('img')
    carImagem.id = 'carImagem'
    carImagem.setAttribute('src','../../static/img/car.png')
    car.appendChild(carImagem)
    square.appendChild(car)

}
function moves(){
    const buttonMoveRight = document.getElementById('buttonnMoveRight')
    const buttonMoveLeft = document.getElementById('buttonnMoveLeft')
    
    buttonMoveRight.onclick = moveRight()
}

function moveRight(){
    const car = document.getElementById('car')
    const move = document.getElementById(`id${RandomNumber +1},${randomNumber2 +1}`)
    move.appendChild(car)
}
