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