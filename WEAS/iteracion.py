# Iteracion

# ¿Cuántas A hay en una palabra?
palabra = "paralelepipedo"
cantidad_de_a = 0
for letra in palabra:
    if letra == "a":
        cantidad_de_a += 1
print(f"La palabra tenia {cantidad_de_a} A")

# ¿Cuántas veces repito algo?
for i in range(5):
    print("Hola")

# Imprimir uno a uno los elementos de una lista

lista_para_las_compras = [
    "Confort", "Toallitas humedas", "Mantequilla"
]

for elemento in lista_para_las_compras:
    print(elemento)

# ¿Cuantas A hay en mi lista de las compras?
lista_para_las_compras = [
    "Confort", "Toallitas humedas", "Mantequilla", "Almendras"
]
cantidad_de_a = 0
for elemento in lista_para_las_compras:
    for letra in elemento:
        if letra.casefold() == "a".casefold():
            cantidad_de_a += 1
print(f"La lista de las compras tenia {cantidad_de_a} A")