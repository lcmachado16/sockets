from socket import * 
serverName = '127.0.0.1' 
serverPort = 12000

# create a socket object
#  AF_INET: address family, IPv4
# SOCK_DGRAM: datagram-based protocol (UDP)
clientSocket = socket(AF_INET,SOCK_DGRAM) 
message = input('Input lowercase sentence:')
# encode the message into bytes
message = message.encode()
# send the message to the server
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom( 2048)
print(modifiedMessage)
clientSocket.close()

#fim 