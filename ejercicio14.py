class Carta:
    def _init_(self, rango, simbolo):
        self.rango = rango
        self.simbolo = simbolo
        
    def _eq_(self, carta):
        if self.rango == carta.rango and self.simbolo == carta.simbolo:
            return True
        return False
        
    def _lt_(self, carta):
        if self.rango == carta.rango:
            return self.simbolo < carta.simbolo
        return self.rango < carta.rango

    def _gt_(self, carta):
        if self.rango == carta.rango:
            return self.simbolo > carta.simbolo
        return self.rango > carta.rango
    
    def _str_(self):
        return f"La carta tiene rango {self.rango} y símbolo {self.simbolo}"

signos = [chr(9824), chr(9825), chr(9826), chr(9827)] # Pica, Corazón, Diamante, Trébol
rangos = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
          "J":11,"Q":12,"K":13,"A":14}

trebol_1, rango_1 = signos[3], rangos["8"]
corazon_2, rango_2 = signos[1], rangos["3"]
pica_3, rango_3 = signos[0], rangos["8"]

carta_1 = Carta(rango_1, trebol_1)
carta_2 = Carta(rango_2, corazon_2)
carta_3 = Carta(rango_3, pica_3)

print(carta_1)
print(carta_2)
print(carta_3)
print(carta_1 > carta_2)
print(carta_1 == carta_2)