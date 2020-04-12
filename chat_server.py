from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( 'DE1_SoC' )
#hostName = gethostbyname( 'DESKTOP-A30LB1P' )LAPTOP-F1G4V6S7

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            #retrieve public key and private key from the received message (message is a string!)
            pk = [int(i) for i in data.split() if i.isdigit()]
            public_key_e=pk[0]
            public_key_n=pk[1]
            print ('public key is : %d, %d'%(public_key_e,public_key_n))
        else:
            cipher=int(data)
            print (str(cipher)+':')
            ###################################your code goes here#####################################
            #data_decoded is the decoded character based on the received cipher, calculate it using functions in RSA.py
            data_decoded = decrypt(pk, cipher)
            print (data_decoded)
            #python2: print data ,
sys.ext()
#What could I be doing wrong?

