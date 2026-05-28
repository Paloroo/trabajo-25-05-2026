localidades_disponible = 200
ventas_neto = 0
Capacidad_maxima = 200

print("¡Bienvenido al sistema de gestion de localidades del teatro.")

ejecución = True
while ejecución: 
    print("\n=============================================")
    print("                       MENÚ PRINCIPAL")
    print("=============================================")
    print("1. Localidades disponibles")
    print("2. vender localidades")
    print("3. Devolver localidades")
    print("4. Historial de ventas")
    print("5. Salir")
    print("================================================")

    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
        if opcion == 1:
            print(f"\n [INFO] Localidades actualmente disponibles: {localidades_disponible}")
    except ValueError:
        print("")