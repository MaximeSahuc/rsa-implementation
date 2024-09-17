#info serveur
N=12345678910111213
E=8952

#Message
M=1621325881510040

#Calcul M^E
Temp=M**E

#Message chiffré(Reste de la division de Temp par N)
Message_chiffré = Temp % N

print(Message_chiffré)
