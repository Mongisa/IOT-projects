from machine import ADC, Pin

class LDR:
    """Questa classe legge un valore da un resistore dipendente dalla luce (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100, GAMMA=0.7, RL10=50, RES=2000, VCC=3.3, RANGE=4095, CONFIG=0):
        """
        Inizializza una nuova istanza.
        :param pin Un pin a cui è collegato un LDR.
        :param min_value Un valore minimo che può essere restituito dal metodo value().
        :param max_value Un valore massimo che può essere restituito dal metodo value().
        :param GAMMA Gamma di assorbimento della luce.
        :param RL10 Resistenza a 10 lux.
        :param RES Valore resistenza in serie con LDR.
        :param VCC Tensione utilizzata.
        :param RANGE Valore massimo che può restituire la lettura.
        :param CONFIG Configurazione del circuito. 0 -> LDR connesso a VCC, 1 -> LDR connesso a GND.
        """
        if min_value >= max_value:
            raise Exception('Il valore minimo è maggiore o uguale al valore massimo')

        # inizializza ADC (conversione da analogico a digitale)
        # crea un oggetto ADC
        self.adc = ADC(Pin(pin))
        self.min_value = min_value
        self.max_value = max_value
        self.GAMMA = GAMMA
        self.RL10 = RL10
        self.RES = RES
        self.VCC = VCC
        self.RANGE = RANGE
        self.CONFIG = CONFIG

    def read(self):
        """
        Legge un valore grezzo dall'LDR.
        :return un valore da 0 a 4095.
        """
        return self.adc.read()
    
    def value(self):
        """
        Legge un valore dall'LDR nell'intervallo specificato.
        :return un valore dall'intervallo specificato [min, max].
        """
        return (self.max_value - self.min_value) * self.read() / 4095
    def lux(self):
        """
        Calcola il valore di lux in base alla resistenza dell'LDR.
        :return un valore di lux.
        """

        GAMMA = self.GAMMA; #Gamma di assorbimento della luce
        RL10 = self.RL10; #Resistenza a 10 lux
        RES = self.RES; #Valore resistenza in serie con LDR
        VCC = self.VCC; #Tensione utilizzata
        RANGE = self.RANGE #Valore massimo che può restituire la lettura

        analogValue = self.read();
        voltage = analogValue / RANGE * VCC;
        resistance = 0
        if self.CONFIG == 0:
            resistance = RES * (VCC - voltage) / voltage; #LDR connessa a VCC
        else:
            resistance = RES * voltage / (VCC - voltage) #LDR connessa a GND
        lux = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA))/10;
        return lux