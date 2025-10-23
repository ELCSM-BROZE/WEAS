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
    pass

def delete_persona():
    pass

while True:
    print(
        """
        ===========================================
                    Gestor de persona
        ===========================================
        1.Crear Persona
        2.Lista Personas
        3.salir
        """
    )
    opcion = input("Ingrese una opcion [1-2-3]: ")
    if opcion == "1":
        create_persona()
    elif opcion == "2":
        read_persona()
    elif opcion == "3":
        print("BYE..")
        break
    else:
        print("Ingrese una opcion valida")
        input("Precione ENTER para continuar.......")
        