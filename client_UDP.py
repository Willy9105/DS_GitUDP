# -*- coding: utf-8 -*-

import socket

ip='192.168.0.202'      #adresse ip du serveur
port= 5005         #port du serveur


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)

sock.sendto("cinema",(ip,port))     #Envoi de la chaine de caracteres "cinema" vers le serveur


trameReponse,addr=sock.recvfrom(1024)           #Permet de recevoir un message qui provient du serveur avec un buffer de taille 1024

print "Réception de la trame de réponse", trameReponse.encode("hex")       #On affiche le message que l'on a reçu en hexa

b0=trameReponse.encode("hex") #On met la trame dans une variable

code=int(b0, 32)    
print "Le code est :", str(code)



