const progressScroll = document.querySelector("#progress-scroll");
const scrollable =
  document.documentElement.scrollHeight - window.innerHeight;

window.addEventListener("scroll", () => {
  const scrolled = window.scrollY;
  progressScroll.style.width = ` ${(scrolled * 80) / scrollable}%`;
});

const faixa = document.getElementById('faixa')
for(let i = 0; i<13;i++){
    const tirinhaInclinada = document.createElement('div')
    tirinhaInclinada.className = "tirinhaInclinada"
    
    faixa.appendChild(tirinhaInclinada)
}
