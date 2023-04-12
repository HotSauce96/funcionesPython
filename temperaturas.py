# Función para calcular la temperatura media de el valle de aburrá a partir de 20 datos diarios de temperatura por 8 días diferentes. 

# Los datos al ser del mismo tipo (Int o Float, según se decida) van a ir en una lista.
# La media es lo mismo que el promedio, por lo que se tomarían las 20 diferentes temperaturas, se sumarían y se dividirían por 20 para tener un promedio de la temperatura del día.
# Luego se tomarían los 8 promedios de los días calculados y se podría promediar igual la temperatura de la semana por ejemplo. 

# La lista valores_diarios tendrá las 20 temperaturas y con la función sum() de python se suman los elementos de la lista y se dividen por 20, luego se almacena el resultado en la variable promedio_dia

def calcular_temp():
	
#Lista vacía que toma los valores del día (20) a través de un ciclo for que crea un diccionario que toma el input del usuario y lo guarda en cada posición.

#Luego con la función sumar de python suma la lista valores_dia y lo divide en el numero_diario_temperaturas

    valores_dia = []
    numero_diario_temperaturas = 20
	
    for i in range(0, numero_diario_temperaturas):
        temperatura = {}
        temperatura["primer_dia"] = int(input("Ingrese la primer temperatura: "))
        valores_dia.append(temperatura["primer_dia"])
        
    promedio_dia = sum(valores_dia) / numero_diario_temperaturas
    
    print(f"el promedio del día fue: {promedio_dia}")


    # dias_semana = 4
    
    # promedio_semana = []
    
    # for i in range(0, dias_semana):
    #     valores_semana = []
    #     valores_semana.append(valores_dia)
        
    #     promedio_semana = sum(valores_semana) / dias_semana

calcular_temp()
