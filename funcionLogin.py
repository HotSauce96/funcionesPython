# Función de Login:

def Login():
    
    #Se declara la variable intentos y se inicia en 0
    
    intentos = 0

    #Se crea ciclo while para que itere hasta que el nombre sea "admin o Admin" y la contraseña "admin123*"

    while True:
        nombre = input("Ingrese usuario: ") # Prompt para pedir nombre 
        contrasena = input("Ingrese contraseña: ") # Prompt para pedir contraseña

    # Validación de las variables nombre y contraseña 

        if nombre == "Admin" or nombre == "admin"  and contrasena == "admin123*":
            print("Hola, bienvenido admin")
            return True
       
    # Si se va por el else, la variable intentos se auto incrementa en uno. 
        else: 
            intentos += 1
            print(f"Los datos no coinciden, intenta de nuevo, llevas {intentos} intentos")
    
   # Se llama la función.
    
Login()
