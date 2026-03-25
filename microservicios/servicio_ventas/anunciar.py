import redis

r = redis.Redis(host='localhost', port=6379, db=0)

venta_id = "202"
# Publica el ID de la venta en el canal
r.publish('ventas_canal', f"Venta ID: {venta_id} - Exitosa")
print(f"Anuncio de venta {venta_id} enviado.")
