#fichier Enguerran

################
#### Objectifs
################

"""Le but du Hackeur est de pouvoir déchiffré le message chiffré 
du client par la clé publique du serveur
On définie :
n=p*q
e : nombre premier avec PHI(n)
PHI(n) = (p-1)*(q-1)
d = inverse de e
M = message
C = reste de la division euclidienne de M**e par n -> message chiffré
M**e % C(n)
PGCD = 1 pour e et PHI(n)

méthode : retrouver(n,d) à partir de (n,e) et faire Cd(mod n)"""


################
#### importation
################


################
#### définition variables
################

n = 703
e = 329
cle_priv = 0
msg_chiffre = 294
phi_n=1

################
#### définition fonction
################

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def est_premier(n) :
  for i in range(2,n) :
    if (n%i) == 0 :
      return False
  return True

# a revoir
def compose_premier(n) :
  for p in range (n+1) :
    for q in range (n+1) :
      if q*p == n and q != n and p != n :
        break
    if q*p == n and p != n and q != n:
        break
  print("q=",q," p = ",p)
  phi_n = (p-1) * (q-1)
  return q,p,phi_n
  

def calc_d(e, phi_n):
    from egcd import egcd
    return egcd(e, phi_n)[1] % phi_n

def trouver_cle_priv(message_chiffre) :
    print("0")
    q,p,phi_n = compose_premier(n)
    if pgcd(e,phi_n) == 1 : 
      print("phi n =",phi_n)
      print("1")
      
      if est_premier(q) is True :
        print("2")
        print("est premier q",q)
        if est_premier(p) is True :
          print("3")
          print("est premier p",p)
          d = 1/e
          print("is OK")
          return d
          
    else :
      print("e n'est pas premier bolosse")


def dechiffrement(mess_chiffre) :
  d = trouver_cle_priv(msg_chiffre)
  print("d =",d)
  print("n =", n)
  print("msg_chiffre = ",msg_chiffre)
  print("msg_chiffre**d = ", msg_chiffre**d)
  print("msg_chiffre**d % n = ", (msg_chiffre**d)%n)
  c = (msg_chiffre**d)%n
  print("c =",c)
  return c

################
#### programme principale
################

#compose_premier(n)
#print(trouver_cle_priv(msg_chiffre))
print(dechiffrement(msg_chiffre))
