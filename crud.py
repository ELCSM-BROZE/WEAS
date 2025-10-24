from datetime import date

class Persona:
    def __init__(
                 self,
                 rut: str,
                 nombre: str,
                 apellido: str,
                 fecha_nacimiento: date,
                 cod_area: int,
                 telefono: int

                 
    ):
        self.rut:str = rut
        self.nombre:str = nombre
        self.apellido:str = apellido
        self.fecha_nacimiento:date = fecha_nacimiento
        self.cod_area:int = cod_area
        self.telefono:int = telefono

def __str__(self):
    return f"{self.rut} {self.nombre} {self.apellido} {self.fecha_nacimiento} {self.cod_area} {self.telefono}"
        

personas: list[Persona]=[]

def persona_existe(persona_nueva: Persona) -> bool:
    for persona in personas:
        print("Persona existe")
        return True
    print("Persona no existe")
    return False

def create_persona():              
    rut: str = input("Ingrese el rut de la persona: ")
    nombre: str = input("Ingrese los nombres de la persona: ")
    apellido: str = input("Ingrese los apellidos de la persona: ")
    dia_nacimiento: date = date (input("Ingrese dia de nacimiento: "))
    mes_nacimiento: date = date (input("Ingrese mes de nacimiento: "))
    anio_nacimiento: date = date (input("Ingrese año de nacimiento: "))
    fecha_nacimiento: date = date(
        year=anio_nacimiento,
        month=mes_nacimiento,
        day=dia_nacimiento
    )
    cod_area: int = int (input("Ingrese codigo de area de su localidad: "))
    telefono: int = int (input("Ingrese telefono de la persona: "))
    persona = Persona(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        cod_area=cod_area,
        telefono=telefono
    )

    if persona_existe(persona):
        return print(f"La persona con el rut {persona.rut} ya existe. Intenete con otro rut.")

    personas.append(persona)


def read_persona():
    for persona in personas:
        print(persona)

def update_persona():
    rut = print("")
    for persona in personas:
        if persona.rut == rut:
            while True:
                print(f"""
                    ===========================================
                    ||        actualizador de persona        ||
                    ===========================================
                    1.rut: {persona.rut}
                    2.nombre: {persona.nombre}
                    3.apellido: {persona.apellido}
                    4.fecha de nacimiento: {persona.fecha_nacimiento}
                    5.codigo de area: {persona.cod_area}
                    6.telefono: {persona.telefono}
                    0.no seguir modificando
                    """
                    )
                opcion = input("¿Que dato quieres modificar?")
                if opcion == "1":
                    rut: str = input("Ingrese el rut de la persona: ")
                    if persona_existe(persona):
                        return print(f"La persona con el rut {persona.rut} ya existe. Intenete con otro rut.")
                    persona.rut = rut
                    print("Rut modificado correctamente ")
                elif opcion == "2":
                    persona.nombre = nombre
                    nombre: str = input("Ingrese los nombres de la persona: ")
                    print("Nombre actualizado correctamente")
                elif opcion == "3":
                    persona.apellido = apellido
                    apellido: str = input("Ingrese los apellidos de la persona: ")
                    print("Apellido actualizado correctamente")
                elif opcion == "4":
                    dia_nacimiento: date = date (input("Ingrese dia de nacimiento: "))
                    mes_nacimiento: date = date (input("Ingrese mes de nacimiento: "))
                    anio_nacimiento: date = date (input("Ingrese año de nacimiento: "))
                    fecha_nacimiento: date = date(
                        year=anio_nacimiento,
                        month=mes_nacimiento,
                        day=dia_nacimiento
                        )
                    persona.fecha_nacimiento = fecha_nacimiento
                    print("fecha de nacimiento se actualizo correctamente")
                elif opcion == "5":
                    persona.cod_area = cod_area
                    cod_area: int = int (input("Ingrese codigo de area de su localidad: "))
                    print("Codigo de area actualizado correctamente ")
                elif opcion == "6":
                    persona.telefono = telefono
                    telefono: int = int (input("Ingrese telefono de la persona: "))
                    print("Telefono actualizado correctamente ")
                elif opcion == "0":
                    break
    print()

def delete_persona():
    rut_busqueda = input("Ingrese el rut de la persaona a editar (E): ")
    for persona in personas:
        if persona.rut:
            print(f"Eliminando persona: {persona}")
            personas.remove(persona)
            print(f"Persona con rut {rut_busqueda} eliminado exitosamente")
    print(f"persona con rut {rut_busqueda}, no encontrada")
    input("Precione ENTER para continuar......")

while True:
    print(
        """
        ===========================================
                    Gestor de persona
        ===========================================
        1.Crear Persona
        2.Lista Personas
        3.Actualizar Personas
        0.salir
        """
    )
    opcion = input("Ingrese una opcion [1-2-3-4-0]: ")
    if opcion == "1":
        create_persona()
    elif opcion == "2":
        read_persona()
    elif opcion == "3":
        update_persona()
    elif opcion == "4":
        delete_persona()
    elif opcion == "0":
        print("BYE..")
        break
    else:
        print("Ingrese una opcion valida")
        input("Precione ENTER para continuar.......")
        