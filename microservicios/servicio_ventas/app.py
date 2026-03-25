import redis

# Conexión a Redis (localhost porque están en la misma máquina virtual)
r = redis.Redis(host='localhost', port=6379, db=0)

def registrar_venta(id_venta, monto):
    r.set(f"venta:{id_venta}", monto)
    print(f"Venta {id_venta} guardada en Redis con monto ${monto}")

registrar_venta("101", "500.00")
