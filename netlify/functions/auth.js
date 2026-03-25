exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      service: "Auth-Service", 
      status: "Funcionando",
      timestamp: new Date()
    })
  };
};
