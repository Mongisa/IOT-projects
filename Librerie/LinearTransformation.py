class LT:
    """
    Classe per la trasformazione lineare di un valore a in un valore b.
    Amin, Amax: limiti del valore di input a
    Bmin, Bmax: limiti del valore di output b
    resolution: numero di decimali da considerare (0 per interi)
    inverse: se True rende la trasformazione inversamente proporzionale
    """
    def __init__(self, Amin=0, Amax=100, Bmin=0, Bmax=100, resolution=0, inverse=False):

        if Bmin > Bmax:
            raise ValueError("Bmin must be less than or equal to Bmax.")
        if Amin > Amax:
            raise ValueError("Amin must be less than or equal to Amax.")
        if resolution < 0:
            raise ValueError("Resolution must be a non-negative integer.")
        self.Amin = Amin
        self.Amax = Amax
        self.Bmin = Bmin
        self.Bmax = Bmax
        self.resolution = resolution
        self.aRange = Amax - Amin
        self.bRange = Bmax - Bmin
        self.scale = self.bRange / self.aRange
        self.inverse = inverse

    def trans(self, a):
        """
        Trasforma il valore di input a in un valore di output b
        a: valore di input da trasformare
        return: valore di output trasformato
        """
        if a < self.Amin:
            a = self.Amin
        if a > self.Amax:
            a = self.Amax
        if self.inverse:
            a = self.Amax - (a - self.Amin)
        b = (a - self.Amin) * self.scale + self.Bmin
        if self.resolution > 0:
            return round(b, self.resolution)
        else:
            return int(b)