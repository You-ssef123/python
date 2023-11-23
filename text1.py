"""nversion_de_type
n= int(input("saisir un nombre entier:"))
p = n**3
print(n,"à la puissance 3 est",p)
r=float(input("entrer un nombre réel:"))
pr=r**3.0
print(r,"a la puissance 3 est",pr)
"""
import math

"""
print("youssef","soufiane","wa","fin",sep="-")
print("bonjour",end=",")
print("wa fin","youssef",sep=" a ",end=".")
"""
"""
x , y = int(input('entrer deux nombres')) ,int(input('entrer deux nombres'))
S = x + y
print('la somme de',x,'et',y,'est:',S)
D = x - y
print('la difference de',x,'et',y,'est:',D)
M = x * y
print('la multiplication de',x,'et',y,'est:', M)
A = x / y
print('la division de',x,'sur',y,'est:',A)
a=int(input("donner un nombre entier"))
s=a**2
print("le resulta est",s)
"""
"""
a = input("donner une valeur")
b = input("donner une valeur")
print("a=",a)
print("b=",b)
a,b=b,a
print("a=",a)
print("b=",b)
print(5%2)
print(2*2*5)
print("yo"*2)
"""
"""
a = 3
b = 5
print("produit est:",a*b)
c = str(b)
print("produit est:", a*c)
"""
"""
y = "youssef"
a = y[0]
print(a)
b = y[0:7:2]
print(b)
print(y[-3:-1])
"""
"""
a = int(input("donner un nombre"))
if a>0 :
    print("la valeur est positif")
elif a==0 :
    print("la valeur est nul")
else :
    print("la valeur est negatif")
print("au revoir")
"""
"""
a = int(input("donner un nombre"))
b = int(input("donner un nombre"))
c = int(input("donner un nombre"))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
"""
"""
A = float(input('entrer le premier nombre'))
B = float(input('entrer le deusième nombre'))
if A>0 :
    if B>0 :
        print('le produit de',A,'et',B,'est positif')
    elif B<0 :
        print('le produit de',A,'et',B,'est negatif')
    else :
        print('le produit de',A,'et',B,'est nul')
elif A == 0 :
    print('le produit de',A,'et',B,'est nul')
else :
    if B>0 :
        print('le produit de',A,'et',B,'est negatif')
    elif B<0 :
        print('le produit de',A,'et',B,'est positif')
    else :
        print("le produit de:",A,"et",B,"est nul")
"""
"""
noteDoral = int(input("donner la note d-orale"))
noteDecrit = int(input("donner la note d-ecrit"))
noteGenerale = (noteDoral+(2*noteDecrit))/3
print("la note generale est:", noteGenerale)
if noteGenerale>=10 :
    print("module validé")
else :
    print("module n-est pas validé")
"""
"""
leSexe = input("donner le sexe dhabitants(homme/femme)")
if leSexe=="homme" :
    lage = int(input("donner lage dhomme"))
    if lage>=20 :
        print("paient")
    else :
        print("ne paient pas")
elif leSexe=="femme" :
    lage = int(input("donner lage du femme"))
    if 18<=lage<=35 :
        print("paient")
    else :
        print("ne paient pas")
else :
    print("ne paient pas")
a = int(input("donner un nombre"))
while a >= 0:
    a = int(input("donner un nombre"))
print("au revoir")
"""
"""
for i in range(1,11):
    print("bonjour")
"""
"""
n = int(input("donner le nombre de repetition"))
for i in range(1,n+1):
    print(i)
"""
"""
n = int(input("donner un nombre entier"))
s = 0
for i in range(0, n+1):
    s = (s + i)
print(s)
"""
"""
s = 0
p = int(input("donner un  nombre"))
while p == 1 :
    p = int(input("donner un nombre"))
for i in range(1,p+1) :
    if p%i==0 :
        s = s+1
if s==2 :
    print(p,"est premier")
else :
    print(p,"nest pas premier")
"""
"""
n = int(input('entrer le premier entier'))
m = int(input('entrer le deusième entier'))
D = 0
S = 0
for A in range(2,n) :
    if n%A == 0 :
        D += A
print('la somme des diviseurs de',n,'est:',D)
for B in range(2,m) :
    if m%B == 0 :
        S += B
print('la somme des diviseurs de',m,'est:',S)
if D==m and S==n :
    print(n,'et',m,'sont des amis')
else :
    print(n,'et',m,'ne sont pas des amis')
"""
"""
a = int(input("donner un nombre"))
s = 0
for i in range(1, a):
    if a % i == 0:
        print(i)
        s = s + i
if s == a:
    print("le nombre est parfait")
else:
    print("le nombre nest pas parfait")
"""
"""
a = int(input("donner un nombre"))
for i in range(1,a+1) :
    b = str(i)
    print("*"*i)
"""
"""
n = int(input("donner un nombre"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n = int(input("donner un nombre"))
for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    for l in range(n, i, -1):
        print("", end="")
    print()
for i in range(1, n + 1):
    for j in range(n, i, -1):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    for l in range(n, i, -1):
        print(" ", end="")
    print()
"""
"""
a = int(input("donner un nombre"))
for i in range(1,a+1) :
    for c in range(1,a+1):
        b = str(i)
        print(c*" ","*"*i)
"""
"""
n = int(input("donner un nombre"))
for i in range(n, 0, -1):
    print('*' * i)
    for l in range(n+1,i, -1):
        print(" ", end="")
print()
for i in range(2, n + 1):
    print('*' * i)
    for l in range(n,i, -1):
        print(" ", end="")
print()
"""
"""
n = int(input("donner un nombre"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n = int(input("donner un nombre"))
for i in range(n,1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")

    print()
for i in range(1,n+1,1):
    for k in range(n+1,i,-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
"""
"""
n = int(input("donner un nombre"))

# Partie supérieure du motif
for i in range(n, 1, -1):
    # Imprime des espaces avant les étoiles
    for j in range(n-i):
        print(" ", end="")

    # Imprime les étoiles
    for k in range(0, i):
        print("*", end="")

    # Imprimer des espaces après les étoiles
    for a in range(1, n, 1):
            print(" ", end="")

    # Passe à la ligne suivante
    print()

# Partie inférieure du motif
for i in range(1, n + 1):
    # Imprime des espaces avant les étoiles
    for j in range(n-i):
        print(" ", end="")

    # Imprime les étoiles
    for k in range(0, i):
        print("*", end="")

    # Imprimer des espaces après les étoiles
    for a in range(n,1,-1):
            print(" ", end="")

    # Passe à la ligne suivante
    print()
"""
"""
def somme(a) :
    s = 0
    for i in range (1,a+1):
        s = s+i
    return s

x = int(input("donner une deusième valeur"))
d = somme(x)
print(d)
"""
"""
def somme(a) :
    s = 0
    for i in range (1,a+1):
        s = s+i
    print(s)

x = int(input("donner une deusième valeur"))
somme(x)
"""
"""
def plus_grand(a,b):
    if (a>b) :
        return a
    elif (a<b)  :
        return b

x = int(input("donner une valeur"))
y = int(input("donner une autrre valeur"))
z = plus_grand(x,y)
print(z)
"""
"""
def pgcd(a,b):
    for i in range (1,min(a,b)+1):
        if a%i==0 and  b%i==0:
            pgcd=i
    return pgcd

x = int(input("donner une valeur"))
y = int(input("donner une autrre valeur"))
d=pgcd(x,y)
print(d)
"""
"""
def numbre(a):
    s=0
    while(a!=0):
        a=a//10
        s=s+1
    return s
c = int(input("donner un nombre"))
while (c != 0):
    d = numbre(c)
    print("le nombre de chiffre est", d)
    c = int(input("donner un nombre"))
"""
"""
def nombre(n):
    n_str = str(n)
    return len(n_str)
    
a = int(input("donner un nombre"))
k = nombre(a)
print(k)
"""
"""
def suite(a,n):
    for i in range (1,n+1):
        s = 0
        z = (a**i)/i
        s = s+z
        return s

b = int(input("donner un nombre"))
p = int(input("donner la puissance"))
d = suite(b,p)
print(d)
"""
"""
def puissance(p,n):
    s = 0
    for i in range(1,n+1):
        s=s+i**p
    return s
b = int(input("donner un nombre"))
a = int(input("donner la puissance"))
d = puissance(a,b)
print(d)
"""
"""
def cube(n):
    s = 0
    while(n!=0):
        n=n//10
        s=n**3+s
    return s
c = int(input("donner un nombre"))
d = cube(c)
print(d)
"""
"""
def cube(n):
    if 100 <= n <= 999:
        nbrC = n // 100
        nbrD = (n // 10) % 10
        nbrU = n % 10
        somme = nbrC**3 + nbrD**3 + nbrU**3
        if somme == n:
            return 1
        else:
            return 0
    else:
        return 0

c = int(input("donner un nombre"))
d = cube(c)
print(d)
"""
"""
def factoriel(n):
    s = 1
    for i in range(1,n+1):
        s = i * s
    return s

c=int(input("donner un nombre"))
d = factoriel(c)
print(d)
"""
"""
def is_odd(num):
    return num%2 != 0
def fact(num):
    if(num == 1):
        return num
    else:
        return num * fact(num-1)
def func_s(num):
    if not is_odd(num) or num <5:
        return -1
    result = 0
    for i in range (1,num+1):
        result+=1 / fact(i)
    return  result
u_num = int(input("please enter a number: "))
print("S(",u_num, ") = ",func_s(u_num), sep="")
"""
"""
def fct(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fct(n - 1) + fct(n - 2)


i = int(input("donner une valeur"))
d = fct(i)
print(d)
"""
"""
def remplir(n,T):
    for i in range(0, n):
        T.append(int(input("donner une valeur")))

def afficher(n, T):
    for i in range(0, n):
       print(T[i],end=" | ")
def min(n,T):
    min = T[0]
    for i in range(0,n):
        if (T[i]<min):
            min = T[i]
    return min
def max(n,T):
    max = T[0]
    for i in range(0,n):
        if (T[i]>max):
            max=T[i]
    return max

remp = 0
choix = 6
while choix>=1 and choix<=7 :
    print("--------Menu---------")
    print("1- Remplir le tableau")
    print("2- Afficher le tableau")
    print("3- Chercher min")
    print("4- Chercher max")
    print("5- Tri par selection")
    print("6- Tri par insertion")
    print("7- Tri par permutation")
    print("8- Quitter")
    choix = int(input("Taper votre choix"))
    if choix == 1:
        print("1- Remplir le tableau")
        n = int(input("donner la taille"))
        tab=[]
        remplir(n,tab)
        remp = 1
    elif choix == 2:
        if remp == 1:
            print("2- Afficher le tableau")
            afficher(n,tab)
        else:
            print("cous devez remplir le tableau")
    elif choix == 3:
        if remp == 1:
            print("3- Chercher min")
            print(min(n,tab))
        else:
            print("cous devez remplir le tableau")
    elif choix == 4:
        if remp == 1:
            print("4- Chercher max")
            print(max(n,tab))
        else:
            print("cous devez remplir le tableau")
    elif choix == 5:
        if remp == 1:
            print("5- Tri par selection")
        else:
            print("cous devez remplir le tableau")
    elif choix == 6:
        if remp == 1:
            print("6- Tri par insertion")
        else:
            print("cous devez remplir le tableau")
    elif choix == 7:
        if remp == 1:
            print("7- Tri par permutation")
        else:
            print("cous devez remplir le tableau")
    else:
        print("8- Quitter")
"""
"""
# Variables
choix = 0
n = 0
Tab = []

# Procedure Remplir
def Remplir(n, T):
    for i in range(n):
        val = int(input("donnez une valeur: "))
        T.append(val)

# Procedure afficher
def afficher(T):
    for val in T:
        print(val, end=" ")
    print()

# Function min
def mini(T):
    x = T[0]
    for i in range(len(T)):
        if T[i] < x:
            x = T[i]
    return x

# Function max
def maxi(T):
    y = T[0]
    for i in range(len(T)):
        if T[i] > y:
            y = T[i]
    return y

# Function selection
def selection(T):
    for i in range(len(T) - 1):
        pmin = i
        for j in range(i + 1, len(T)):
            if T[j] < T[pmin]:
                pmin = j
        T[i], T[pmin] = T[pmin], T[i]
    return T

# Function insertion
def insertion(T):
    for i in range(1, len(T)):
        tmp = T[i]
        j = i
        while j > 0 and T[j - 1] > tmp:
            T[j] = T[j - 1]
            j -= 1
        T[j] = tmp
    return T

# Function permutation
def permutation(T):
    change = True
    while change:
        change = False
        for i in range(len(T) - 1):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                change = True
    return T

# Main Program
while choix < 8:
    print("MENU\n 1-Remplir tableau\n 2-Afficher tableau\n 3-Recherche Min\n 4-Recherche Max\n 5- Tri par insertion\n 6- Tri par sélection\n 7- Tri par permutation\n 8- Quitter\n")
    choix = int(input("Taper votre choix: "))

    if choix == 1:
        print("1-Remplir tableau")
        n = int(input("entrez la taille du tableau: "))
        Tab = []
        Remplir(n, Tab)

    elif choix == 2:
        print("2-Afficher tableau")
        afficher(Tab)

    elif choix == 3:
        print("3-Recherche Min")
        ABS = mini(Tab)
        print("le plus petit nombre dans le tableau est:", ABS)

    elif choix == 4:
        print("4-Recherche Max")
        D = maxi(Tab)
        print("le plus grand nombre dans le tableau est:", D)

    elif choix == 5:
        print("5- Tri par insertion")
        Tab = insertion(Tab)
        print("Tableau trié:", Tab)

    elif choix == 6:
        print("6- Tri par sélection")
        Tab = selection(Tab)
        print("Tableau trié:", Tab)

    elif choix == 7:
        print("7- Tri par permutation")
        Tab = permutation(Tab)
        print("Tableau trié:", Tab)

    elif choix == 8:
        print("Au revoir")

    else:
        print("Choix invalide. Veuillez choisir un numéro de 1 à 8.")
"""

"""
import translate
from translate import Translator
data = Translator(from_lang="french",to_lang="English")
res = data.translate("bonjour")
print(res)
"""
from gtts import gTTS
txt = "welcome in my channel"
langue = "en"
res = gTTS(text=txt,lang=langue)
res.save("audio.mp3")


