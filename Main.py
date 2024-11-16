import random # Importamos el módulo que usaremos para generar el número.

minimo = 1 # Valor predeterminado para el número aleatorio.

dificultad = input("Escoge el nivel de dificultad: (F,M,D) ").upper() # Aquí se le pide al usuario que escoja un nivel de dificultad y convierte lo asignado en mayúsculas.
if dificultad == "F":
    maximo = 15
elif dificultad == "M":
    maximo = 65
elif dificultad == "D":    # Dependiendo de la dificultad el rango que se puede generar es mayor.
    maximo = 135
elif dificultad not in "FMD":  # Si la dificultad no es válidad mostrará un mensaje de error.
    print("Error en la dificultad") 
    maximo = 15    # Si la dificultad no es válidad tendrá un valor predeterminado el rango.

numeroAlAzar = random.randint(minimo, maximo) # Aquí se va a generar el número aleatorio dependiendo rango mínimo y el máximo.
intentos = 0 # Se inicializa el contador de los intentos.

# El bucle principal del programa.
while True:
   intentosUsuario = int(input("Introduce un número: ")) # Solicitamos al usuario un número y lo convertimos a un número entero.
   intentos += 1 # Los intentos se incrementarán cada que el usuario introduzca un número hasta encontrar el correcto.

   # Aquí compara el número que el usuario insertó con el número que se generó al azar.
   if intentosUsuario > numeroAlAzar:
    print("El número es menor del que proporcionaste!")

   elif intentosUsuario < numeroAlAzar:
    print("El número es mayor del que proporcionaste!")
   else:
    break  # Si el usuario acierta saldrá del bucle.

print("Enhorabuena! has acertado." + str(intentos)) # Mensaje que saldrá una vez se haya acertado el número junto al número de intentos. 



