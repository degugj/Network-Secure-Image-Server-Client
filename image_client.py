import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt
import struct


SERVER_IP    = gethostbyname( 'DE1_SoC' )
PORT_NUMBER = 5000
SIZE = 1024
des_key='secret_k'
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
#generate public and private key from the p and q values
p=1297507
q=1298053
public, private = generate_keypair(p, q)

#send public key
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
message=('des_key')
mySocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))

#send des_key
#encode the DES key with RSA and save in DES_encoded
des_encoded = []
for character in des_key:
    des_encoded.append(str(encrypt(private, character)))
[mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in des_encoded]






# for keybyte in des_key:
#     characterArr = [str(i) for i in keybyte]
#     character = int("".join(messageArr))
#     des_encoded.append(str(encrypt(private, chr(character))))
#     mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))


#new des object
newdes = des.des()

#read image, encode, send the encoded image binary file
file=open(r'penguin.jpg',"rb") 
data=file.read()
file.close()
#print(data)
#r_byte=bytearray(data, 'utf-8')
#print(r_byte)
#print(len(r_byte))
#i = 1
#byteArray = []
#resultArray = []
#for byte in r_byte:
#    byteArray.append(byte)
#    if i == 8:
#        resultArray.append(newdes.encrypt(des_key, byteArray, False, False, 'ASASASAS'))
#        i = 0
#        byteArray = []
#    i+=1

#r_byte = resultArray
#creating bit array from byte array
# bitArray = []
# for byte in r_byte:
#     for bit in byte:
#         bitArray.append(bit)

#encrypting every 64 bits
# x = 0
# bitArray64 = []
# for i in bitArray:
#     bitArray64[i] = bitArray[i]
#     if x==64:
#         x = 0
#         r_byte.append(newdes.encrypt(des_key, bitArray64, False, False, 'ASASASAS'))
#         bitArray64 = []
#     x+=1


encryptedData = newdes.encrypt(des_key, data)
r_byte = bytes(encryptedData, "ISO-8859-1")

# def encrypt(self, key, text, padding=False,cbc=False,IV='ASASASAS'):
 


###################################your code goes here#####################################
#the image is saved in the data parameter, you should encrypt it using des.py
#set cbc to False when performing encryption, you should use the des class
#coder=des.des(), use bytearray to send the encryped image through network
#r_byte is the final value you will send through socket


#send image through socket

mySocket.sendto(r_byte,(SERVER_IP,PORT_NUMBER))
print('encrypted image sent!')

