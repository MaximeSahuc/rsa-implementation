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
msg_chiffre = 162


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

def compose_premier(n) :
  for p in range (n+1) :
    for q in range (n+1) :
      if q*p == n and q != n and p != n :
        break
    if q*p == n and p != n and q != n:
        break
  print("q=",q," p = ",p)
  phi_n = (p-1) * (q-1)
  if pgcd(e,phi_n) == 1 :
     print("alez")
     return q,p,phi_n

def calc_d(e, phi_n):
    from egcd import egcd
    return egcd(e, phi_n)[1] % phi_n

def exponentiation_modulaire(a, e, n):
  p=1
  while e>0:
    if e % 2 == 1:
       p = (p*a)%n
    a=(a*a)%n
    e=e//2
  return p


def dechiffrement(mess_chiffre) :
  q,p,phi_n = compose_premier(n)
  print("e =",e)
  print("phi n =",phi_n)
  d = calc_d(e, phi_n)
  print("d =",d)
  print("n =", n)
  print("msg_chiffre = ",msg_chiffre)
  print("msg_chiffre**d = ", msg_chiffre**d)
  print("msg_chiffre**d % n = ", (msg_chiffre**d)%n)
  c = exponentiation_modulaire(msg_chiffre,d,n)
  print("c =",c)
  return c

################
#### programme principale
#####

print(dechiffrement(msg_chiffre))
