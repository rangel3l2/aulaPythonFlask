function getData(){
    const req = new XMLHttpRequest()
    req.open("GET", "http://10.8.39.157:5000/api-teti?token=ABC",false)
    req.send()
    req.console.error('server unconected');
    return req.responseText
}
function resultado(){
    const resultado = document.getElementById('resultado')
    let dados = getData()
    
    resultado.innerHTML = `<h2> ${dados}</h2>`
    
}
