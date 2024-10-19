import socket
import threading

Host = '127.0.0.1'
Port = 12346

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Host, Port))
server_socket.listen()
clients = []
usernames = []

# Fonction pour diffuser un message à tous les clients sauf l'émetteur
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message.encode('utf-8'))

# Fonction pour gérer les messages privés (mp)
def mp(message_str):
    message_tuple = message_str.split(' ')
    
    # Format attendu : "mp from sender to receiver message_content"
    if len(message_tuple) >= 5 and message_tuple[0] == 'mp' and message_tuple[2] == 'to':
        sender = message_tuple[1]
        receiver = message_tuple[3]
        message_content = ' '.join(message_tuple[4:])
        
        if receiver in usernames:
            index = usernames.index(receiver)
            destinater = clients[index]
            private_message = f"Private message from {sender}: {message_content}"
            destinater.send(private_message.encode('utf-8'))
        else:
            print(f"Receiver {receiver} not found.")

# Fonction pour gérer la communication avec un client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            message_str = message.decode('utf-8')
            if message_str.startswith('mp'):
                mp(message_str)
            else:
                broadcast(message_str, client)
        except Exception as e:
            
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            print(f'The user {username} has quit the chat.')
            broadcast(f'{username} has left the chat.', client)
            usernames.remove(username)

# Fonction pour accepter les nouveaux clients
def receive():
    while True:
        client, address = server_socket.accept()
        print(f'Connecting with {address}')
        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)
        print(f'Username of the client is {username}')
        
        broadcast(f'{username} has joined the chat.', client)
        client.send('Connected to the server.'.encode('utf-8'))

        # Démarrage d'un nouveau thread pour gérer ce client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Server is listening...')
receive()
