import socket
import threading

Host= '127.0.0.1'
Port= 8080

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((Host, Port))
server_socket.listen()
clients=[]
usernames=[]
    
def broadcast(message, _client):
    for client in clients:
       if client!=_client:
          client.send(message)

def handle_client(client):
   while True:
      try:
         message = client.recv(1024)
         broadcast(message, client)
      except:
         index= clients.index(client)
         clients.remove(client)
         client.close()
         username=usernames[index]
         print(f'The user {username} has quite the chat.'.encode('utf-8'),None)
         usernames.remove(username)
         break 
    
def receive():
    while True:
      client, addrs= server_socket.accept()
      print(f'connecting with {addrs}')
      client.send('USERNAME'.encode('utf-8'))
      username= client.recv(1024).decode('utf-8')
      usernames.append(username)
      clients.append(client)
      print(f' username of the client is {username} ')
      broadcast(f' {username} has joined the chat '.encode('utf-8'), client)
      client.send('connected to the server '.encode('utf-8'))

      thread = threading.Thread(target=handle_client, args=(client,))
      thread.start()

print('server is Listening...')
receive()