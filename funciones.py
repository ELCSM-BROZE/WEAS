# Funciones
# 1er paso es definir la funcion
# def nombre_de_funcion(argumento1, argumento2):
#       paso1
#       paso2
#       paso3
#       return valor
#
#
# 2do paso es llamar a la funcion
# nombre_de_funcion(valor1, valor2)


# Contador de una letra en especifico
def contador_de_letra_en_especifico(letra_a_contar: str, palabra: str):
    cantidad_de_coincidencias = 0
    for letra in palabra:
        if letra.casefold() == letra_a_contar.casefold():
            cantidad_de_coincidencias += 1
    return cantidad_de_coincidencias


# Recursividad
def suma(a: int, b: int) -> int:
    return a+b

print( suma(suma(1, 5), suma(2, 5)) )

# Funcion sin return

def imprimir_mensaje_personalizado(nombre: str) -> None:
    print(
        f"""
        {"="*41}
        {nombre.center(41, "/")}
        {"="*41}
        """
    )
imprimir_mensaje_personalizado("Sebastian")