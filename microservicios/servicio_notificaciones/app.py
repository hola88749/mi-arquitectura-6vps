import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def procesar_notificacion(id_venta):
    monto = r.get(f"venta:{id_venta}")
    if monto:
        print(f"NOTIFICACIÓN: Se ha procesado la venta {id_venta} por un valor de ${monto.decode('utf-8')}")
    else:
        print("Venta no encontrada")

procesar_notificacion("101")
