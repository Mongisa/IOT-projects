s="Inserisci un numero intero positivo: "
n=int(input(s))

while n < 0:
    n=int(input(s))

i=0
for c in str(n):
    i += 1

print("Il numero di cifre è: ", i)