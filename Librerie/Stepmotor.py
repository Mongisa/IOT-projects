from machine import Pin
from time import sleep

class Stepmotor:
    def __init__(self,in1,in2,in3,in4, minSpeed=0.0009, maxSpeed=0.09):
        """
        Costruttore della classe Stepmotor.
        
        :param in1: Pin di controllo 1
        :param in2: Pin di controllo 2
        :param in3: Pin di controllo 3
        :param in4: Pin di controllo 4
        :param minSpeed: Velocità minima del motore (in secondi per passo)
        :param maxSpeed: Velocità massima del motore (in secondi per passo)
        """
        self.inPins = [Pin(in1, Pin.OUT), Pin(in2, Pin.OUT), Pin(in3, Pin.OUT), Pin(in4, Pin.OUT)]
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

        self.halfStepSequence = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        self.fullStepSequence = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1]
        ]
    
    def step(self, direction, steps, speed, half=False):
        """
        Esegue i passi del motore in una direzione specificata.
        :param direction: Direzione del movimento (1 per avanti, -1 per indietro)
        :param steps: Numero di passi da eseguire
        :param speed: Velocità del motore (in %)
        """
        if speed < 0:
            speed = 0
        elif speed > 100:
            speed = 100
        sleepTime = self.minSpeed + (self.maxSpeed - self.minSpeed) * (speed / 100)
        
        if half:
            sequence = self.halfStepSequence
        else:
            sequence = self.fullStepSequence
        for i in range(steps):
            index = (i + direction) % len(sequence)
            for j in range(4):
                self.inPins[j].value(sequence[index][j])
        # Aspetta il tempo necessario per il passo
        sleep(sleepTime)