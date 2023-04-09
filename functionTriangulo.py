# Función para solicitar una base y una altura de un triángulo y mostrar su área y perímetro 

def mostrarTriangulo():
     
    base = int(input("Ingrese por favor la base o el ancho: "))
    altura = int(input("Ingrese por favor la altura: "))
    
    print("Para hallar el perímetro necesitamos saber la medida de los lados del triangulo")
    
    ladoUno = int(input("Ingrese por favor el primer lado: "))
    ladoDos = int(input("Ingrese por favor el segundo lado: "))
    ladoTres = int(input("Ingrese por favor el tercer lado: "))
     
    print("Debemos recordar que el área de un triángulo es base  * altura / 2; y que su perímetro se calcula como: Perimetro = Lado + Lado + Lado ")
    
    print("Debido a que existen diferentes tipos de triángulos, (Escaleno, Isoceles, Equilátero) La fórmula del perímetro no puede ser P = L * 3 (No todos lados tienen el mismo valor)")
    
# Se realizan las fórmulas de área y perímetro: 

    a = (base * altura) / 2
    p = ladoUno + ladoDos + ladoTres
    
    print(f"El área del rectángulo es: {a} y su perímetro es: {p}")
     

# Se llama a la función: 

mostrarTriangulo()
