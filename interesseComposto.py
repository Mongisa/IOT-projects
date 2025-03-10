ci=float(input("Inserisci il capitale iniziale: "))
tia=float(input("Inserisci il tasso di interesse annuo: "))
na=float(input("Inserisci il numero di anni: "))

if ci <= 0 or na <= 0:
    print("I parametri immessi non sono corretti!")
    exit()

imf=ci*(1+tia/100)**na

print("L'importo finale è %f" % imf)