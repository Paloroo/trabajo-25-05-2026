while True:
    try:
        cantidad = int(input("¿Cuántos usarios desea registrar?: "))
        if cantidad > 0:
            break
        print("Debe ingresar al menos 1 usuario.")
    except ValueError:
        print("¡Error! Debe ingresar un numero entero.")

Normales = 0
uso_alto = 0

for i in range(cantidad):
    print(f"\n--- Registro de usuario {i+1} ---")

    while True:
        nombre = input("Ingrese el nombre del usuario (minimo 4 letras y sin espacios): ")

        if " " in nombre: 
            print("El nombre no debe contener espacios.")
        elif len(nombre):
            print("El nombre debe contener mínimo 4 letras (caracteres).") 
        else:
            break
        
    while True:
        try:
                horas = float(input(f"¿Cuántas horas se conecto el el usuario {nombre}?: "))
                if horas >= 0:
                    break
        except:            
            print("¡Erro! lo que debe contener es un numero entero y no puede ser reemplazado por un caracter.")