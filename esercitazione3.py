class Veicolo:
    def __init__(self, marca, modello, anno, vel_max):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.vel_max = vel_max
    
    def __str__(self):
        return "%s %s (%d) - Velocità massima: %d km/h" % (self.marca, self.modello, self.anno, self.vel_max)
    
    def descrizione(self):
        print("Veicolo: ",self.__str__())

    def tipo_veicolo(self):
        return "Generico Veicolo"

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, vel_max,num_posti):
        super().__init__(marca, modello, anno, vel_max)
        self.num_posti = num_posti

    def __str__(self):
        return "Auto: %s - %d posti" % (super().__str__(),self.num_posti)

    def descrizione(self):
        print(self.__str__())
    
    def tipo_veicolo(self):
        return "Automobile"

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, vel_max, ha_sidecar):
        super().__init__(marca, modello, anno, vel_max)
        self.ha_sidecar = ha_sidecar

    def __str__(self):
        return "Moto: %s - %s" % (super().__str__(), "Con sidecar" if self.ha_sidecar else "Senza sidecar")
    
    def descrizione(self):
        print(self.__str__())

    def tipo_veicolo(self):
        return "Motocicletta"

v1=Auto("Toyota","Corolla",2020,180,5)
v2=Moto("Harley Davidson","",2019,220,False)

v1.descrizione()
v2.descrizione()

def mostra_descrizione(veicolo):
    veicolo.descrizione()

mostra_descrizione(v1)
mostra_descrizione(v2)

class Camion(Veicolo):
    def __init__(self, marca, modello, anno, vel_max,cap_car):
        super().__init__(marca, modello, anno, vel_max)
        self.cap_car = cap_car
    
    def __str__(self):
        return "Camion: %s - Capacità: %d tonnellate" % (super().__str__(), self.cap_car)
    
    def descrizione(self):
        return print(self.__str__())

v3=Camion("Volvo","FH16",2021,140,25)

v3.descrizione()