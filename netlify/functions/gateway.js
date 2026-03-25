exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      service: "Conserflow-Gateway", 
      status: "Online",
      description: "Administrador central de peticiones",
      node: "Tehuacán-Server-01"
    })
  };
};
