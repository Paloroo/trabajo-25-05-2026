print("#######Bienvenido/a a la cafeteria universitaria######")
menu_comprobante = False
Fondo_fijo = 150000 
egreso = 0
ingreso = 0 
fondo_neto = 0
while not menu_comprobante:
    print("################ MENU UNIVERSITARIO ################")
    print("1. Ver saldo de la caja.")
    print("2. Registro de egreso.")
    print("3. Registro de ingreso.")
    print("4. Ver balance neto.")
    print("5. Cerrar caja y Salir.")
    print("#######################################################")
    try:
        opt = int(input("Ingrese una opción: "))
    except ValueError:
        print("¡Error! debe ser un numero entero") 
    else:
        if opt == 1:
            print(f"El saldo de la caja es: {Fondo_fijo}")
        elif opt == 2:
            egreso_comprobante = False
            while not egreso_comprobante:
                try:
                    egreso_sacado = int(input("Ingrese cuanta plata saco de la caja: "))
                    if egreso_sacado > 0 and egreso_sacado < Fondo_fijo:
                        Fondo_fijo -= egreso_sacado
                        fondo_neto -= egreso_sacado
                        egreso_comprobante = True
                    else:
                        print("¡Error! no puede sacar mas de lo que tiene en caja y no puede sacar 0 o cantidad negativa.")
                except ValueError:
                    print("¡Error! No debe ser caracter.") 
        elif opt == 3:
            ingreso_comprobante = False
            while not ingreso_comprobante:
                try:    
                    ingreso_agregado = int(input("Ingrese cuanta plata dejo en la caja: "))
                    if ingreso_agregado > 0 and ingreso_agregado + Fondo_fijo < 500000:
                        Fondo_fijo += ingreso_agregado
                        fondo_neto += ingreso_agregado
                        ingreso_comprobante = True
                    else:
                        print("¡Error! NO debe superar los 500000 CLP, operación rechazada.")       
                except ValueError:
                    print("¡Error! No debe contener caracteres.")              
        elif opt == 4:
            print(f"El balance neto es de: {fondo_neto}")
        elif opt == 5:
             print("Gracias por utilizar nuestro software, hasta la proxima.")    
             menu_comprobante = True                        #los try & except se usan solo en int(input)