from xmlrpc.server import SimpleXMLRPCServer

def consultar_saldo(quantidade_inicial, quantidade_vendida):
    return quantidade_inicial - quantidade_vendida

servidor= SimpleXMLRPCServer(("localhost", 8002))

servidor.register_function(
    consultar_saldo,
    "consultar_saldo"
)

print("Servidor RPC aguardando solicitações...")

servidor.serve_forever()
