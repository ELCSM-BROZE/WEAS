# Bucles

# Bucles infinitos o Mientras/Hasta que
# while

palabra_secreta = "123pormi"
protegido = True

while protegido:
    print("No puedes pasar, debes de adivinar la palabra secreta")
    intento = input("Ingresa la palabra secreta: ")

    if intento == palabra_secreta:
        input("Palabra acertada. Ingrese ENTER para continuar...")
        protegido = False
    else:
        print("Incorrecto, intente nuevamente...")



# Bucles finitos o Por cada
# for in

mensaje = "Hola mundo"
cantidad_de_veces_a_escribir = 5
# i = Indice
# Indice controla la posicion en la que estoy
for i in range(cantidad_de_veces_a_escribir):
# Range se ocupa cuando es un valor numerico
    print(mensaje)
