import socket
import threading

host = '127.0.0.1'
port = 8080

def message_client(client):
    while True:
              try:
                     message = client.recv(1024).decode('utf-8')
                     if message:
                            print(message)
                     else:
                            break
              except:
                     break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

thread = threading.Thread(target=message_client, args= (client,))
thread.start()

while True:
       message= input()
       client.send(message.encode('utf-8'))