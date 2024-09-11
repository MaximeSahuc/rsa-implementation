#info serveur
N=703
E=329

#Message
M=986512476

#Calcul M^E
Temp=M**E

#Message chiffré(Reste de la division de Temp par N)
Message_chiffré = Temp % N

print(Message_chiffré)
