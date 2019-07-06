#start with a range
#explore the space with few bits
#reduce the range and increase the bits
#exploration / exploitation

class chromosomeManipulation(object):
    def __init__(self, lo: float, hi: float, k: int):
        self.lo = lo
        self.hi = hi
        self.k = k
        self.hilo = hi-lo

    def dec2bin(self, x: float) -> list:
        result = []
        sign = 1 if x < 0 else 0
        integer = int(abs(x)*2**self.k)
        while integer > 1:
            result.append(integer % 2)
            integer //= 2 
        result.append(integer)
        result.append(sign)
        return result

    def bin2dec(self, x: list) -> float:
        result = 0.0
        for i in range(len(x)-1):
            result += x[i]*2**(i-self.k)
        return -result if x[-1] == 1 else result

    def normalize(self, x: float) -> float:
        result = (x-self.lo)/self.hilo
        if result > 1.0:
            result = 1.0
        elif result < 0.0:
            result = 0.0
        return result

    def de_normalize(self, x: float) -> float:
        return x*self.hilo+self.lo

    def to_chromosome(self, x: float) -> list:
        return self.dec2bin(self.normalize(x))
    
    def from_chromosome(self, x: list) -> float:
        return self.de_normalize(self.bin2dec(x))
    
    def update(self, lo: float, hi: float, k: int):
        self.lo = lo
        self.hi = hi
        self.k = k
        self.hilo = hi-lo
