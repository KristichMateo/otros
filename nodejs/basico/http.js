const http = require('http');
const handleServer = function(req, res){
    res.writeHead(200,{'Content-type':'text/html'});
    res.write("<h1>Hola mudo</h1>");
    res.end();
} 
const server = http.createServer(handleServer);
server.listen(3000,function(){
    console.log("todo correcto en el puerto 3000");
});
