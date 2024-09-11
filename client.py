#info serveur
N=551
E=

#Message
M=89865

#Calcul M^E
Temp=M**E

#Message chiffré(Reste de la division de Temp par N)
Message_chiffré = Temp % N

print("Message_chiffré")
