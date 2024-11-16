import random

minimo = 1

dificultad = input("Escoge el nivel de dificultad: (F,M,D) ").upper()
if dificultad == "F":
    maximo = 15
elif dificultad == "M":
    maximo = 65
elif dificultad == "D":
    maximo = 135
elif dificultad not in "FMD":
    print("Error en la dificultad") 
    maximo = 10

numeroAlAzar = random.randint(minimo, maximo)
intentos = 0


while True:
   intentosUsuario = int(input("Introduce un número: "))
   intentos += 1

   if intentosUsuario > numeroAlAzar:
    print("El número es menor del que proporcionaste!")

   elif intentosUsuario < numeroAlAzar:
    print("El número es mayor del que proporcionaste!")
   else:
    break

print("Enhorabuena! has acertado." + str(intentos))



