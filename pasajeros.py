"""
datos_pasajeros = [
    (nombre1, cedula1, destino1),
    (nombre2, cedula2, destino2),
    (nombre3, cedula3, destino3),
    ....
    (nombreN, cedulaN, destinoN)
]

datos_cuidad = [
    (ciudad1, pais1),
    (ciudad2, pais2),
    (ciudad3, pais3),
    ....
    (ciudadN, paisN)
]
"""

datos_pasajeros = []
datos_cuidad = []

while True:
    try: 
        print("\t.:Menu:.")
        print("Opciones:")
        print("1. Ingresar datos de pasajeros")
        print("2. Revisar datos de pasajeros por cedula")
        print("3. Revisar numero de pasajeros por cuidad")
        print("4. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            nombre = input("Ingrese nombre: ")
            cedula = input("Ingrese cedula: ")
            destino = input("Ingrese destino: ")
            pais = input("Ingrese pais: ")
            datos_pasajeros.append((nombre, cedula, destino))
            datos_cuidad.append((destino, pais))
        elif opcion == 2:
            if len(datos_pasajeros) == 0:
                print("No hay datos de pasajeros")
            else:
                cedula = input("Ingrese cedula: ")
                for pasajero in datos_pasajeros:
                    if pasajero[1] == cedula:
                        print("Nombre: ", pasajero[0])
                        print("Cedula: ", pasajero[1])
                        print("Destino: ", pasajero[2])
        elif opcion == 3:
            if len(datos_cuidad) == 0:
                print("No hay datos de ciudad")
            else:
                destino = input("Ingrese destino: ")
                cuenta = 0
                for cuidad in datos_cuidad:
                    if cuidad[0] == destino:
                        cuenta += 1
                print("Numero de pasajeros que viajan a: ", destino, "es: ", cuenta)
        elif opcion == 4:
            print("Gracias por usar el codigo")
            break
    except ValueError:
        print("Opcion no valida")
        opcion = int(input("Ingrese una opcion: "))