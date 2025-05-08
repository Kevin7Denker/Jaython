import socket
import threading

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    clients.append(conn)
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = f"[{addr[0]}:{addr[1]}] {data.decode()}".encode()
            print(msg.decode())
            broadcast(msg, conn)
    except:
        pass
    finally:
        print(f"[DESCONECTADO] {addr}")
        clients.remove(conn)
        conn.close()

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[ESPERANDO CONEXÕES] Servidor ouvindo em {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    HOST = "10.20.23.215"
    PORT = 2612
    start_server(HOST, PORT)
