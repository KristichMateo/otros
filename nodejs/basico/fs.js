const fs = require('fs');
fs.writeFile('./archivo.txt','Hola mundo', (err)=>{
    if (err){
        console.log("error")
    }else{
        console.log("Archivo creado")
    }
})