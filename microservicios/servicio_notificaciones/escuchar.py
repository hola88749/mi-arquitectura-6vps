import redis

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()

# Se suscribe al canal "ventas_canal"
p.subscribe('ventas_canal')

print("Esperando nuevas ventas en tiempo real...")

for mensaje in p.listen():
    if mensaje['type'] == 'message':
        print(f"¡ALERTA RECIBIDA! Nueva venta procesada: {mensaje['data'].decode('utf-8')}")
