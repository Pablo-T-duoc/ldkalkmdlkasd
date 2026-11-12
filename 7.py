investigador_Asistente = 0
investigador_Principal = 0

print("==== BIENVENIDO AL SISTEMA DE REGISTROS DE CIENTÍFICOS ====\n")

# Pedir una cantidad válida antes de iniciar el registro.
while True:
    try:
        cientificos = int(input("Ingrese la cantidad de científicos a registrar: "))
    except ValueError:
        print("Error: ingresa un número entero positivo.")
        continue

    if cientificos > 0:
        break
    print("Dato inválido: ingresa un entero mayor que cero.")

for i in range(1, cientificos + 1):
    print(f"\n===== Registrando científico {i} de {cientificos} =====")

    while True:
        id_Cientifico = input("Ingrese un ID de al menos 12 caracteres: ").strip()
        if len(id_Cientifico) >= 12:
            print("Ingresaste un ID válido.")
            break
        print("Error: el ID debe contener al menos 12 caracteres. Inténtalo nuevamente.")

    while True:
        try:
            num_Publicaciones = int(input("Número de publicaciones del científico: "))
        except ValueError:
            print("Error: ingresa un número entero mayor o igual que cero.")
            continue

        if num_Publicaciones >= 0:
            break
        print("Error: el número de publicaciones no puede ser negativo.")

    # Clasificar una sola vez, después de validar las publicaciones.
    if num_Publicaciones >= 12:
        print("Clasificado como investigador principal.")
        investigador_Principal += 1
    else:
        print("Clasificado como investigador asistente.")
        investigador_Asistente += 1

# Mostrar los totales al finalizar todos los registros.
print("\n" + "=" * 65)
print(f"Investigadores principales: {investigador_Principal}")
print(f"Investigadores asistentes: {investigador_Asistente}")
print("=" * 65)
