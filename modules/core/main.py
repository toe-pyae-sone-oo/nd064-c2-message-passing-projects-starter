import grpc
import time
from concurrent import futures
import udaconnect_pb2_grpc
from rpcservices import PersonServicer


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
udaconnect_pb2_grpc.add_PersonServicer_to_server(PersonServicer(), server)

SERVER_PORT = 5005

print(f"Server starting on port {SERVER_PORT}...")
server.add_insecure_port(f"[::]:{SERVER_PORT}")
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
