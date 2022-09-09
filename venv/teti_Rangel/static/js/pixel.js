$.ajax({
    type: "POST",
    url: '/pixel',
    datatype : JSON,
    data: {
    
        
        action: 'randomColors'
    },
    success : function(response){
        
        color = response.resulted
        createPixelColor(color)
        
    },
    error: ((response)=>{
        console.log(`response${response}`)

    })
})
    
                      
    
async function createPixelColor(color){  
    try{
        const container = document.getElementById('container')
        const squares = document.createElement('div')
        squares.id = 'squares'
        container.appendChild(squares)
    for(let i = 0; i<512; i++){
        for(let j = 0; j<512; j ++){
            const square = document.createElement('div')
            square.className = 'square'
            square.id = `id${i}`
            squares.appendChild(square) 
            square.style.backgroundColor = await color[i][j]

    }
   

    }
    }catch(error){
    console.log(error)
}
}