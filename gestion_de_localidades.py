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

        elif opcion == 2:
            try:
                cantidad = int(input("Ingrese la cantidad de localidades que quiere vender: "))
                if cantidad > 0:
                    if cantidad <= localidades_disponible:
                        localidades_disponible -= cantidad
                        ventas_neto += cantidad
                        print(f"¡Venta exitosa! se han vendido {cantidad} localidades")
                    else:
                        print("¡Error! No hay suficientes localidades para esta venta.")
                else:
                    print("¡Error! la cantidad debe ser un numero entero mayor a cero.")
            except ValueError:
                print("¡Error! Ingrese un número entero válido para la cantidad.")

        elif opcion == 3:
            try:
                cantidad = int(input("Ingrese la cantidad de localidades a devolver: ")) 
                if cantidad > 0:
                    if localidades_disponible + cantidad <= Capacidad_maxima:
                        localidades_disponible += cantidad
                        ventas_neto -= cantidad
                        print(f"¡Devolución exitosa! Se ham reincorporado {cantidad} las localidades.")
                    else:    
                        print("¡Error! No se puede devolver esa cantidad. Supera la capacidad máxima del teatro ({Capacidad_maxima})")
            except ValueError:
                print("¡Error! Ingrese un número entero vlaido para la cantidad.")

        elif opcion == 4: 
            print(f"\n[HISTORIAL] Total de ventas netas de la sesion: {ventas_neto} entradas.")

        elif opcion == 5: 
            print("\nGracias por utilizar nuestro software, hasta la próxima.")
            ejecutando = False
        else:
            print("¡Error! Opcion fuera de rango, Seleccione un numero entre 1 y 5.")
    except  ValueError:
        print("¡Error de entrada! Por favor, introduzca únicamente caracteres numéricos en el menú.")