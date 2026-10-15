# Colecciones
list # []
# Guardar una lista de valores por
# orden de llegada, puedo trabajar
# con indices para especificar el dato.

lista_para_las_compras = [
    "Confort", "Toallitas humedas", "Mantequilla"
]

# Leer todos los valores
print(lista_para_las_compras)

# Leer sólo 1 valor. Ejemplo: Toallitas humedas
print( lista_para_las_compras[1] )

# Modificar
print(lista_para_las_compras[2]) # Antes: Mantequilla
lista_para_las_compras[2] = "Margarina" 
print(lista_para_las_compras[2]) # Despues: Margarina

# Agregar elementos
lista_para_las_compras.append("Cilantro")
print(lista_para_las_compras[3])

# Eliminar elemento. Ejemplo: Remover las toallitas humedas
lista_para_las_compras.remove(1)
print(lista_para_las_compras)

# Buscar por valor
indice_confort = lista_para_las_compras.index("Confort") # Resultado: 0
lista_para_las_compras[indice_confort] = "Scott"
print(lista_para_las_compras[indice_confort]) # Resultado: Scott

tuple # ()
# Las tuplas son listas inmutables, osea
# que no se pueden modificar pero si leer.

lista_de_invitados = (
    "Felipe", "Mijael", "Maximiliano", "Luna", "Danitza", "Maria"
)

# Leer todos los valores
print(lista_de_invitados)

# Leer sólo 1 valor. Ejemplo: Mijael
print( lista_de_invitados[1] )

dict # {}
# Diccionarios
# Estructurar data bajo el paradigma Clave: Valor

persona = {
    "nombre": "Sebastian",
    "sede": "Renca",
    "email": "sebastian.morales74@inacapmail.cl",
    "telefono": "+56926864578",
    "cantidad_de_aprobaciones": 24,
    "habilidades": [
        "Python", "Typescript", "Godot Engine"
    ]
}

# Leer los datos
print(persona)

# Leer un dato en especifico
print(persona["nombre"]) # Resultado: Sebastian

# Modificar un dato
print(persona["nombre"]) # Antes: Sebastian
persona["nombre"] = "Ricardo"
print(persona["nombre"]) # Despues: Ricardo

# Agregar un dato
persona["comuna"] = "Quilicura"

# Eliminar un dato
persona.pop("telefono")
print(persona)
