from machine import Pin, ADC
from math import log

class Thermistor:
    """Questa classe legge un valore da un termistore"""

    def __init__(self, pin, min_value=0, max_value=100, BETA=3950):
        """
        Inizializza una nuova istanza.
        :param pin Un pin a cui è collegato un termistore.
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
        self.BETA = BETA

    def read(self):
        """
        Legge un valore grezzo dal termistore.
        :return un valore da 0 a 4095.
        """
        return self.adc.read()
    
    def value(self):
        """
        Legge un valore dal termistore nell'intervallo specificato.
        :return un valore dall'intervallo specificato [min, max].
        """
        return (self.max_value - self.min_value) * self.read() / 4095
    def value_celsius(self):
        """
        Legge un valore dal termistore in gradi Celsius.
        :return un valore in gradi Celsius.
        """
        # Calcola la temperatura in gradi Celsius
        return 1 / (log(1 / (4095 / self.read() - 1)) / self.BETA + 1.0 / 298.15) - 273.15