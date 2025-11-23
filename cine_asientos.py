def crear_sala():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas por fila: "))

    sala = []
    for i in range(filas):
        fila = ["L"] * columnas
        sala.append(fila)

    print("\nSala creada correctamente.\n")
    return sala


def mostrar_sala(sala):
    print("\nSala de cine")
    for fila in sala:
        print(" ".join(fila))
    print()


def reservar_asiento(sala):
    print("\nReservar asiento")
    fila = int(input("Fila: "))
    col = int(input("Columna: "))

    if fila < 0 or fila >= len(sala) or col < 0 or col >= len(sala[0]):
        print("Ese asiento no existe.\n")
        return

    if sala[fila][col] == "L":
        sala[fila][col] = "X"
        print("Asiento reservado correctamente.\n")
    else:
        print("Ese asiento ya está ocupado.\n")


def liberar_asiento(sala):
    print("\nLiberar asiento")
    fila = int(input("Fila: "))
    col = int(input("Columna: "))

    if fila < 0 or fila >= len(sala) or col < 0 or col >= len(sala[0]):
        print("Ese asiento no existe.\n")
        return

    if sala[fila][col] == "X":
        sala[fila][col] = "L"
        print("Asiento liberado correctamente.\n")
    else:
        print("Ese asiento ya está libre.\n")


def contar_asientos(sala):
    libres = 0
    ocupados = 0

    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1

    print("\nEstadísticas de la sala")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")


def menu():
    print("Configuración inicial de la sala")
    sala = crear_sala()

    while True:
        print("MENÚ")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            reservar_asiento(sala)
        elif opcion == "3":
            liberar_asiento(sala)
        elif opcion == "4":
            contar_asientos(sala)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.\n")


menu()
