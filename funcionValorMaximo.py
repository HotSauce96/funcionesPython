# Función de hallar el valor máximo y el valor mínimo dentro de una lista. 

#Convencion Python _

def determinar_valores(lista):
    
# Se declaran variables que van a almacenar los valores, máximo y mínimo

    valor_maximo = lista[0]
    valor_minimo = lista[0]
    
# Se crea el ciclo for con el cuál se va a revisar cada posición de la lista y se va a entrar a comparar primero con la variable valor_maximo, indicando si es mayor el número de la posición que el número que haya tomado valor_maximo, sí es así, lo actualiza hasta que termine la lista. 

# Ocurre inversamente con valor_minimo. 
    
    for i in range(1, len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
        if lista[i] < valor_minimo:
            valor_minimo = lista[i]
            
# Se imprime el valor máximo y mínimo encontrados.

    print(f'Dentro de la lista: {lista} el valor máximo es: {valor_maximo} y el valor mínimo es: {valor_minimo}')
        
# Lista de prueba 

lista = [4, -5, -1, 8, 7, 10, 16]

# Llamada a la función para encontrar el valor máximo y mínimo.

determinar_valores(lista)



# Misma función, pidiendo inputs, con lógica más avanzada: 

#def encontrar_maximo_minimo():
    # Pide al usuario que ingrese una lista de números separados por comas
 #   lista_str = input("Ingresa una lista de números separados por comas: ")
    
    # Convierte la entrada de texto en una lista de números
 #  lista = [int(x) for x in lista_str.split(",")]
    
    # Encuentra el valor máximo y mínimo en la lista
#    maximo = max(lista)
#   minimo = min(lista)
    
    # Devuelve el valor máximo y mínimo como una tupla
#    return maximo, minimo
