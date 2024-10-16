import socket

def MyServeur():
  
  # creation du socket TCP/IP 
  server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

  #Binding socket whith the port 8080 and the networks interface '0.0.0.0'
  server_socket.bind(('0.0.0.0', 8080))

  #listning the input connexion
  server_socket.listen(5)
  print('the serveur is listning all networks connection whith the port:8080')

  #acception for the networks connection
  while True:
    client_socket,client_serveur=server_socket.accept()
    client_ip,client_port=client_serveur
    print('connected in port : {client_port}')
    #send a data to client
    pn= client_socket.recv(1024).decode() 
    message= f'pn*2={int(pn)*2}'
    client_socket.send(message.encode())
    #closing a networks connection
    client_socket.close()
MyServeur()