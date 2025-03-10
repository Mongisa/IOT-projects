#ESERCIZIO 1
ci=float(input("Inserisci il capitale iniziale: "))
tia=float(input("Inserisci il tasso di interesse annuo: "))
na=float(input("Inserisci il numero di anni: "))

if ci <= 0 or na <= 0:
    print("I parametri immessi non sono corretti!")
    exit()

imf=ci*(1+tia/100)**na

print("L'importo finale è %f" % imf)

#ESERCIZIO 2
s="Inserisci un numero intero positivo: "
n=int(input(s))

while n < 0:
    n=int(input(s))

i=0
for c in str(n):
    i += 1

print("Il numero di cifre è: ", i)

#ESERCIZIO 3
s="Inserisci un numero intero positivo: "
n=int(input(s))

while n < 0:
    n=int(input(s))

f=1

for i in range(1,n+1,1):
    f=f*i

print("Il fattoriale di %d è %d" % (n,f))

#ESERCIZIO 4
import math

a=int(input("Inserisci coefficiente a: "))
b=int(input("Inserisci coefficiente b: "))
c=int(input("Inserisci coefficiente c: "))

print("Equazione: %dx^2 + %dx + %d = 0" % (a,b,c))

delta=b**2 - 4*a*c

if delta < 0:
    print("Non esistono soluzioni reali")
    exit()

x1=(-b+math.sqrt(delta))/2*a
x2=(-b-math.sqrt(delta))/2*a

print("x1=%f \nx2=%f" % (x1,x2))