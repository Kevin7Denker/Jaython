import socket
import threading

def send_message_to_server(addr: str, port: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((addr, port))
    
    def receive_messages():
        while True:
            try:
                data = client.recv(1024)
                if data:
                    print(f"\n{data.decode()}\nDigite: ", end="")
            except:
                break

    threading.Thread(target=receive_messages, daemon=True).start()

    try:
        while True:
            message = input("Digite: ")
            if message:
                client.send(message.encode())
    except KeyboardInterrupt:
        print("\n[CLIENTE DESCONECTADO]")
        client.close()

if __name__ == "__main__":
    HOST = "10.20.23.215"
    PORT = 2612
    send_message_to_server(HOST, PORT)
