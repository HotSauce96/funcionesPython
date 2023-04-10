# Función para solicitar una base y una altura de un triángulo y mostrar su área y perímetro 

def mostrarTriangulo():
     
    while True:
    
        base = int(input("Ingrese por favor los cm de la base o el ancho: "))
        altura = int(input("Ingrese por favor los cm de la altura: "))
        
        print("Para hallar el perímetro necesitamos saber la medida de los lados del triangulo")
        
        ladoUno = int(input("Ingrese por favor los cm del primer lado: "))
        ladoDos = int(input("Ingrese por favor los cm del segundo lado: "))
        ladoTres = int(input("Ingrese por favor los cm del tercer lado: "))
        
        print("Debemos recordar que el área de un triángulo es base  * altura / 2; y que su perímetro se calcula como: Perimetro = Lado + Lado + Lado ")
    #"Debido a que existen diferentes tipos de triángulos, (Escaleno, Isoceles, Equilátero) La fórmula del perímetro no puede ser P = L * 3 (No todos lados tienen el mismo valor)
        
    # Se realizan las fórmulas de área y perímetro: 

        a = (base * altura) / 2
        p = ladoUno + ladoDos + ladoTres
        
        if ladoUno == ladoDos and ladoUno == ladoTres: 
            print(f"El área del rectángulo es: {a} cm^2, su perímetro es: {p} cm y es un triángulo equilátero.")
        
        elif ladoUno == ladoDos or ladoDos == ladoTres:
            print(f"El área del rectángulo es: {a} cm^2, su perímetro es: {p} cm y es un triángulo isóceles.")
        else: 
            print(f"El área del rectángulo es: {a} cm^2, su perímetro es: {p} cm y es un triángulo escaleno.")

#Ciclo para mostrar el triángulo 

        for i in range(base):
            linea = ""
            for j in range(i+1):
                linea += "*" # Agregar un asterisco a la línea
            print(linea) # Imprimir la línea en la consola
            
# Se llama a la función: 

mostrarTriangulo()
