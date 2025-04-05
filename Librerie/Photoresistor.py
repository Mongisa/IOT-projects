from machine import ADC, Pin

class LDR:
    """Questa classe legge un valore da un resistore dipendente dalla luce (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100):
        """
        Inizializza una nuova istanza.
        :param pin Un pin a cui è collegato un LDR.
        :param min_value Un valore minimo che può essere restituito dal metodo value().
        :param max_value Un valore massimo che può essere restituito dal metodo value().
        """
        if min_value >= max_value:
            raise Exception('Il valore minimo è maggiore o uguale al valore massimo')

        # inizializza ADC (conversione da analogico a digitale)
        # crea un oggetto ADC
        self.adc = ADC(Pin(pin))
        self.min_value = min_value
        self.max_value = max_value

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