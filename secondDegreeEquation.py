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