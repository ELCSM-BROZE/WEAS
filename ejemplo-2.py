# Continuacion: Herencia y Polimorfismo 
 
class Mascota: 
    def __init__(self, nombre: str, edad: str, peso: float, especie: str, raza: str, sexo: str, fallecido: bool): 
        self.__nombre = nombre 
        self.__edad = edad 
        self.__peso = peso
        self.__especie = especie
        self.__raza = raza
        self.__sexo = sexo
        self.__fallecido = fallecido
 
    def obtenerNombre(self) -> str: return self.__nombre 
    def obtenerEdad(self) -> str: return self.__edad 
    def obtenerPeso(self) -> float: return self.__peso 
    def obtenerEspecie(self) -> str: return self.__especie
    def obtenerRaza(self) -> str: return self.__raza
    def obtenerSexo(self) -> str: return self.__sexo
    def obtenerFallecido(self) -> bool: return self.__fallecido
 
    def modificarPeso(self, nuevo_peso: float) -> None: 
        if nuevo_peso <= 0: 
            print("Peso incorrecto, debe ser mayor que 0.") 
            return 
        self.__peso = nuevo_peso 
 
    mascotas: list[Mascota] = [] 
    for mascota in mascotas: 
        print("---") 

class Perro(Mascota): 
    def __init__(self, nombre: str, edad: str, peso: float, raza: str, sexo: str, fallecido: bool):
        super().__init__(nombre,edad,"Canis lupus familiaris",raza,peso,sexo,fallecido)

class Vaca(Mascota): 
    def __init__(self, nombre: str, edad: str, peso: float, raza: str, sexo: str, fallecido: bool):
        super().__init__(nombre,edad,"Bos taurus",raza,peso,sexo,fallecido)

class Pollito(Mascota): 
    def __init__(self, nombre: str, edad: str, peso: float, raza: str, sexo: str, fallecido: bool):
        super().__init__(nombre,edad,"Gallo",raza,peso,sexo,fallecido)

perro_1 = Perro(
    nombre = "lukita",
    edad="4años y 9 meses",
    raza="dalmata",
    peso=14.5,
    sexo="femenino",
    fallecido=True
)

print(perro_1.obtenerEspecie(),perro_1.obtenerRaza())