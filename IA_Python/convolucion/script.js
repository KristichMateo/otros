let image = new Image();
image.onload = imageLoaded;
image.src = "messi.jpg";
function imageLoaded() {
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    canvas.width = image.width;
    canvas.height = image.height;

    ctx.drawImage(image,0, 0, image.width, image.height)
    blancoYNegro(canvas)
    let resultado = document.getElementById("resultado");
    convolucionar(canvas,resultado)
}
function blancoYNegro() {
    let ctx = canvas.getContext("2d");
    let imgData = ctx.getImageData(0,0,canvas.width,canvas.height)
    let pixeles = imgData.data;
    for (let i = 0; i < pixeles.length; i+=4) {
        let rojo = pixeles[i];   
        let verde = pixeles[i+1];        
        let azul = pixeles[i+2];        
        let alfa = pixeles[i+3];
        let gris = (rojo+verde+azul)/3;        
        pixeles[i]=gris
        pixeles[i+1]=gris
        pixeles[i+2]=gris

    }
    ctx.putImageData(imgData,0,0);
}
function convolucionar(canvasFuente,canvasDestino) {
    
}