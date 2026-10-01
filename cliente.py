from xmlrpc.client import ServerProxy

servidor= ServerProxy("http://localhost:8002/")

resultado= servidor.consultar_saldo(15,4)

print("Unidades restantes:", resultado)
