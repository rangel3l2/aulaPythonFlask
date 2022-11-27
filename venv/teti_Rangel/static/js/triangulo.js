const ladoA = document.getElementById('ladoA');
const ladoB = document.getElementById('ladoB');
const ladoC = document.getElementById('ladoC');
const area = document.getElementById('area');
const maiorLado = document.getElementById('maiorLado');
const perimetro = document.getElementById('perimetro');
const trianguloParaCima = document.getElementById('triangulo-para-cima');

trianguloParaCima.style.borderLeftWidth = `${ladoA.value}px` 
trianguloParaCima.style.borderRightWidth = `${ladoB.value}px`
trianguloParaCima.style.borderBottomWidth = `${ladoC.value}px`

function mudarBorder(e){
    trianguloParaCima.style.borderLeftWidth = `${ladoA.value}px` 
    trianguloParaCima.style.borderRightWidth = `${ladoB.value}px`
    trianguloParaCima.style.borderBottomWidth = `${ladoC.value}px`
}
function maiorLadoF(){
    maiorLado.style.visibility = 'visible'
    perimetro.style.visibility = 'hidden'
    area.style.visibility = 'hidden'
}
function perimetroF(){
    perimetro.style.visibility = 'visible'
    maiorLado.style.visibility = 'hidden'
    area.style.visibility = 'hidden'
}

function areaF(){
    area.style.visibility = 'visible'
    maiorLado.style.visibility = 'hidden'
    perimetro.style.visibility = 'hidden'
}
function enviarDados(e){
    e.preventDefault()
    return false
}
