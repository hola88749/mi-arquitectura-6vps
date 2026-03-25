const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    service: "Auth Service",
    status: "Online",
    message: "Hola desde el microservicio de Autenticación",
    path_received: req.url
  }));
});

server.listen(4001, () => {
  console.log('Microservicio AUTH corriendo en puerto 4001');
});
