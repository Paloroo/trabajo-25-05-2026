cant_vehiculos = int(input("cantidad de autos: "))
print(f"Cuantos autos tienes: {cant_vehiculos}")
if cant_vehiculos > 0:
    print("tiene un vehiculo o mas")
elif cant_vehiculos >= 6:
    print("Tiene seis o mas vehiculos")
else:     
    print("Cantidad invalida, ingrese un numero entero positivo")


for i in range(cant_vehiculos):
    while True:
        try:
            placa_auto = input("Digito y letra de la placa: ")
        except ValueError:
            print("Invalido, Tiene un error el cual no posee letras y numeros.")
        else: 
             if len(placa_auto) >= 6 and " " not in placa_auto:
                 print("Su placa es valida.")
                 break
             else:
                 print("Error deben ser 6 caracteres para la placa y no debe tener espacios.")

while True:
    try:
        Capacidad = int(input("Ingrese la cantidad de carga (en toneladas): "))
        if Capacidad > 0:
            break
        else:
            print("¡Error logistico! Ingresa un numero positivo para la capacidad de carga.")
    except ValueError: 
        print("¡Error logistico! Ingresa un número entero positivo para la capacidad de carga.")
        if Capacidad > 55:
            vehiculos_ligero += 1
        else:
            vehiculos_pesados += 1

print(f"\n¡La flota cuenta con {vehiculos_pesados} vehiculos pesados y {vehiculos_ligero} vehiculos ligeros! ¡Rutas asignadas!")            