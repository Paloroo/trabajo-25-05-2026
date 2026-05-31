
cant_correos = 0
correo_valido = 0
salir = False

while salir == False:

    print("##############Validador de correos###################")
    print("1. Ingresar la cantidad de correos")
    print("2. Ingresar los correos")
    print("3. Salir")
    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        while correo_valido == False:
            try:
                cant_correos = int(input("Ingrese la cantidad de correos que desea validar: "))
            except ValueError:
                print("Valor ingresado incorrecto, intente nuevamente")
            else:
                if cant_correos > 0:
                    correo_valido = True
                else:
                    print("Cantidad no valida, intente nuevamente")

    elif opcion == 2:
        if cant_correos > 0:
            for i in range(cant_correos):
               correo_valido = False
               while correo_valido == False:
                   correo = input("Ingrese el correo que desea validar: ").strip().lower()
                   if "@" in correo and " " not in correo and len(correo)>=6:
                       correo_valido = True
            else:
                print("Correo no valida, intente nuevamente")    

                es_institucional = correo.endswitch("duoc.cl")

                if es_institucional:
                    cantidad_institucional=+1
                else:
                    cantidad_no_institucional+=1

        else:
            print("Debe volver a la primera opcion y agregar el numero de correos que desea validar")

    elif opcion == 3:   
         print(f"La cantidad de correos institucionales es: {cantidad_institucional}")
         print(f"La cantidad de correos no institucionale es: {cantidad_no_institucional}")
    elif opcion == 4:
        print("Salir")
        salir = True
    else:
        print("Gracias, ya posee su correo institucional puede continuar con su uso.")     