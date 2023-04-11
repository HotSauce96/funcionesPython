# Clase suma 
class suma:
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero

    # Metodo de sumar 
    def sumar(self):
        return self.primer_numero + self.segundo_numero

suma_uno = suma(8, 10)
suma_dos = suma(100, 50)
print(suma_uno.sumar(), suma_dos.sumar())

# Clase restar 
class resta: 
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
    
    def restar(self):
        return self.primer_numero - self.segundo_numero

resta_uno = resta(40, 25)
resta_dos = resta(20, 55)
print(resta_uno.restar(), resta_dos.restar())

# Clase multiplicar
class multiplicacion:
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero

    # Metodo de multiplicar 
    def multiplicar(self):
        return self.primer_numero * self.segundo_numero

multiplicacion_uno = multiplicacion(8, 5)
multiplicacion_dos = multiplicacion(12, 5)
print(multiplicacion_uno.multiplicar(), multiplicacion_dos.multiplicar())
