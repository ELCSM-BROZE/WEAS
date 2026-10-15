class Estudiante:
    def __init__(self,nombre:str ,notas: list[float]):
        self.__nombre: str = nombre
        self.__notas: list[float] = notas
        self.__promedio: float = self.__calcularPromedio(self.__notas)
        self.__clasificacion: str = self.__calcularClasificacion(self.__promedio)
#metodo largo

    #def calcularPromedio(notas: list[float]) -> float:
    #    sumatoria_notas = 0
    #    for nota in notas:
    #        sumatoria_notas += nota
    #    promedio = sumatoria_notas / len(nota)
    #    return promedio
#metodo corto
    def __calcularPromedio(notas: list[float]) -> float:
        return sum(notas) / len(notas)

    def __calcularClasificacion(self, promedio: float) -> str:
        if promedio < 4.0: return "Reprobado"
        elif promedio >= 4.0 and promedio <= 4.94: return "Aprobado"
        elif promedio >= 5.0 and promedio <= 5.94: return "Buen rendimiento"
        elif promedio >= 6.0 and promedio <= 7.0: return "Rendimiento destacado"

    def mostarResumen(slef):
        print("estudiante",self.__nombre)
        print("Promedio",self.__promedio)
        print("Clasificacion",self.__clasificacion)