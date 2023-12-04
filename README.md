
# 4: Votaciones de la CONFECH

La CONFECH, en su afán de agilizar el proceso de recuento de las votaciones, le ha encargado el desarrollo de un programa de registro de votación por universidades.
Primero, el programa debe solicitar al usuario ingresar la cantidad de universidades que participan en el proceso.
Luego, para cada una de las universidades, el usuario debe ingresar el nombre de la universidad y los votos de sus alumnos, que pueden ser: aceptar (A), rechazar (R), nulo (N) o blanco (B). El término de la votación se indica ingresando una X, tras lo cual se debe mostrar los totales de votos de la universidad, con el formato que se muestra en el ejemplo.
Finalmente, el programa debe mostrar el resultado de la votación, indicando la cantidad de universidades que aceptan, que rechazan y en las que hubo empate entre estas dos opciones.



`# Definir una estructura para almacenar los votos de cada universidad
class VotosUniversidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aceptar = 0
        self.rechazar = 0
        self.nulo = 0
        self.blanco = 0

### Función para recopilar los votos de las universidades
def recopilar_votos():
    cantidad_universidades = int(input("Ingrese la cantidad de universidades que participan en el proceso: "))
    universidades = []

    for i in range(cantidad_universidades):
        nombre = input("Ingrese el nombre de la universidad: ")
        votos = VotosUniversidad(nombre)
        universidades.append(votos)
    
        while True:
            voto = input("Ingrese el voto de los alumnos (A: aceptar, R: rechazar, N: nulo, B: blanco, X: terminar): ")
    
            if voto == 'A':
                votos.aceptar += 1
            elif voto == 'R':
                votos.rechazar += 1
            elif voto == 'N':
                votos.nulo += 1
            elif voto == 'B':
                votos.blanco += 1
            elif voto == 'X':
                break
            else:
                print("Opción no válida, ingrese una opción válida.")
    
    return universidades

### Función para calcular el resultado de la votación
def calcular_resultado(universidades):
    aceptar = 0
    rechazar = 0
    empate = 0

    for universidad in universidades:
        if universidad.aceptar > universidad.rechazar:
            aceptar += 1
        elif universidad.rechazar > universidad.aceptar:
            rechazar += 1
        else:
            empate += 1
    
    return aceptar, rechazar, empate

### Función principal
def main():
    universidades = recopilar_votos()

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
    main()`
