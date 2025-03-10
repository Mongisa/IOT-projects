s="Inserisci un numero intero positivo: "
n=int(input(s))

while n < 0:
    n=int(input(s))

f=1

for i in range(1,n+1,1):
    f=f*i

print("Il fattoriale di %d è %d" % (n,f))