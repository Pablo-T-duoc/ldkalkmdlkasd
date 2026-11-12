capacidad_maxima = 25
equipos_disponibles = capacidad_maxima
total_equipos_liberados = 0
total_equipos_asignados = 0
salir = 1

while salir == 1:
    print("===== SISTEMA DE GESTIÓN DE EQUIPOS DEL LABORATORIO =====")
    print("1.- Equipos disponibles")
    print("2.- Asignar equipo")
    print("3.- Liberar equipo")
    print("4.- Historial de usos")
    print("5.- Salir")
    print("=" * 60)

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: ingrese un valor entero válido.")
        continue

    match opcion:
        case 1:
            print("La cantidad de equipos disponibles es de", equipos_disponibles)

        case 2:
            try:
                equipo_asignar = int(input("Ingrese una cantidad de equipos a asignar: "))
            except ValueError:
                print("Error: ingrese un valor entero válido.")
                continue

            if equipo_asignar <= 0:
                print("Error: la cantidad debe ser mayor que 0.")
            elif equipo_asignar > equipos_disponibles:
                print("No debe superar la cantidad de equipos disponibles.")
            else:
                # Restar del stock y acumular en el historial.
                equipos_disponibles -= equipo_asignar
                total_equipos_asignados += equipo_asignar
                print(f"Se asignaron {equipo_asignar} equipos.")
                print(f"Equipos disponibles: {equipos_disponibles}")

        case 3:
            try:
                liberar_equipos = int(input("Cantidad de equipos a liberar: "))
            except ValueError:
                print("Error: ingrese un valor entero válido.")
                continue

            equipos_en_uso = capacidad_maxima - equipos_disponibles
            if liberar_equipos <= 0:
                print("Error: la cantidad debe ser mayor que 0.")
            elif liberar_equipos > equipos_en_uso:
                print(f"Error: solo hay {equipos_en_uso} equipos en uso para liberar.")
            else:
                # Devolver al stock y acumular en el historial.
                equipos_disponibles += liberar_equipos
                total_equipos_liberados += liberar_equipos
                print(f"Se liberaron {liberar_equipos} equipos.")
                print(f"Equipos disponibles: {equipos_disponibles}")

        case 4:
            print("====== HISTORIAL DE USOS =====")
            print(f"Equipos asignados en total: {total_equipos_asignados}")
            print(f"Equipos liberados en total: {total_equipos_liberados}")
            print(f"Equipos disponibles: {equipos_disponibles}")
            print(f"Equipos en uso: {capacidad_maxima - equipos_disponibles}")
            print("=" * 60)

        case 5:
            while True:
                try:
                    salir = int(input("\n¿Desea salir? 0) Sí  1) No: "))
                except ValueError:
                    print("Error: ingrese 0 o 1.")
                    continue
                if salir == 0 or salir == 1:
                    break
                print("Opción inválida: ingrese 0 o 1.")

            if salir == 0:
                print("Gracias por utilizar nuestro software, hasta la próxima.")
            else:
                print("Continuamos con los registros...")

        case _:
            print("Opción inválida: ingrese un número entre 1 y 5.")
