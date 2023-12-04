#Define un estructura para almacenar los votos de cada universidad
class VotosUniversidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aceptar = 0
        self.rechazar = 0
        self.nulo = 0
        self.blanco = 0

#Funcion para recopilar los votos de las universidades
def recoplilar_votos():
    cantidad_universidades = int(input("Ingrese la cantidad de universidades que participan en el proceso: "))
    universidades = []

    for i in range(cantidad_universidades):
        nombre = input("Ingrese el nombre de la universidad: ")
        votos = VotosUniversidad(nombre)
        universidades.append(votos)

        while True:
            voto = input("ingrese el voto de los alumnos(A: aceptar, R: rechazar, N: nulo, B: blanco, X: terminar): ")

            if voto == 'A':
                votos.aceptar += 1
            elif voto == 'R':
                votos.rechazar += 1
            elif voto ==  'N':
                votos.nulo += 1
            elif voto == 'B':
                votos.blanco += 1
            elif voto == 'X':
                break
            else:
                print("Opcion no Valida, ingrese una opcion valida")

    return universidades
# Funcion para calcular el resultado de la votacion

def calcular_resultado(universidades):
    aceptar = 0
    rechazar = 0
    empate = 0

    for universidad in universidades:
        if universidad.aceptar > universidad.rechazar:
            aceptar +=1
        elif universidad.rechazar > universidad.aceptar:
            rechazar += 1
        else:
            empate += 1
    return aceptar, rechazar , empate


#funcion principal
def main():
    universidades = recoplilar_votos()
    for universidad in universidades:
        print("\nResultado de la votación en {}:".format(universidad.nombre))
        print("Aceptar: {}".format(universidad.aceptar))
        print("Rechazar: {}".format(universidad.rechazar))
        print("Nulo: {}".format(universidad.nulo))
        print("Blanco: {}".format(universidad.blanco))
    
    aceptar, rechazar, empate = calcular_resultado(universidades)
    print("\nResultado general de la votación:")
    print("Aceptan: {}".format(aceptar))
    print("Rechazan: {}".format(rechazar))
    print("Empate: {}".format(empate))

if __name__ == "__main__":
    main()
