import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message: {message}")
                broadcast_message(message, client_socket)
        except:
            break

    client_socket.close()

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    host = '127.0.0.1'  # localhost
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server started on {}:{}".format(host, port))

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        print(f"Client connected: {address[0]}:{address[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

clients = []

if __name__ == '__main__':
    start_server()