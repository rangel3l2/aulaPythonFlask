import math

class Triangulo:
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0
        
    def getPerimetro(self):
        return self.ladoA+self.ladoB+self.ladoC
        
    
    def getMaiorLado(self):
        return  max(self.ladoA, self.ladoB, self.ladoC)
    def getArea(self):
        return self.ladoA*self.ladoB*self.ladoC
        # perimetro = int(self.getPerimetro/2)
        # p = perimetro
        # A   = self.ladoA
        # B  = self.ladoB
        # C   = self.ladoC
        # area = math.sqrt(p*(p-A)*(p-B)*(p-C))
        # return float(f"{area:2f}")
    

    
        
        
