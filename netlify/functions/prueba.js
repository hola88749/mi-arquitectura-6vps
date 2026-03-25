exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      status: "Conserflow Online", 
      mensaje: "Microservicio de prueba ejecutado con éxito",
      autor: "Gerardo Merchant"
    })
  };
};
