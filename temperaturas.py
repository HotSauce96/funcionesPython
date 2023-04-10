# Función para calcular la temperatura media de el valle de aburrá a partir de 20 datos diarios de temperatura por 8 días diferentes. 

# Los datos al ser del mismo tipo (Int o Float, según se decida) van a ir en una lista.
# Estadísticamente hablando, la media es lo mismo que el promedio, por lo que se tomarían las 20 diferentes temperaturas, se sumarían y se dividirían por 20 para tener un promedio de la temperatura del día.
# Luego se tomarían los 8 promedios de los días calculados y se podría promediar igual la temperatura de la semana por ejemplo. 

# La lista valores_diarios tendrá las 20 temperaturas y con la función sum() de python se suman los elementos de la lista y se dividen por 20, luego se almacena el resultado en la variable promedio_dia

def calcular_temperatura(valores_diarios):
	
	suma = sum(valores_diarios)
	promedio_dia = suma / 20
	print(f"El promedio del día fue de: {promedio_dia}")
	
	promedio_semana = promedio_dia * 8 / 8 # La multplicación serían los otros 8 promedios de los días, en este ejemplo solo para mostrar la fórmula ya que la respuesta no tiene sentido.  
	
	print(f"El promedio de la semana fue de: {promedio_semana}")

# Para calcular el promedio de la semana necesitaríamos entonces 8 promedios del día (Es decir la suma de 8 listas que tienen 20 valores cada una)
# La fórmula del promedio de la semana sería igual promedio_semana = promedio_dia + promedio_dia_dos ... / 8
# Como se necesitarían 20 listas en el parámetro de la función no quedaría limpio ni legible; y cuando se pide una lista en un input se deben separar los valores con comas para poder ser procesados por un ciclo for con el método split().

calcular_temperatura([36, 34, 38, 36, 34, 30, 25, 34, 28, 29, 32, 36, 35, 30, 27, 26, 34, 36, 29, 34])
