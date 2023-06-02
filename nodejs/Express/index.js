const express = require('express');
const morgan = require('morgan');
const app = express();


app.all('/users',(req, res, next)=>{    //Para todo lo que pase por esta ruta ejecuta este callback
    console.log("funcionoooooooooo");       
    next();                             //Segui con las otras rutas
})
function middleware (req, res, next){
    console.log(`tu ruta es: ${req.protocol} ://${req.get('host')}${req.originalUrl}`)
    next()
}
app.use(middleware);
app.use(morgan('dev'));
app.use(express.json());            //Para que pueda leer JSON (middleware)

app.get('/users',(req, res)=>{           //app.metodo y nombre de la ruta, y su callback
    res.send('Hola mundoddd')
})
app.post('/users/:id',(req, res)=>{ //Para ruta personalizadas usarmos :nombre_var       
    res.send('peticion post');      // y para manipularlo-> req.params
    console.log(req.params);        // req.body para ver el json que me estan mandando
    console.log(req.body)
})
app.put('/',(req, res)=>{
    res.send('Peticion update')
})
app.delete('/',(req, res)=>{
    res.send('Peticion de eliminacion')
})
app.listen(3000,()=>{
    console.log("Hola mundo")
} )