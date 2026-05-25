cant_vehiculos = int(input("cantidad de autos: "))
print(f"Cuantos autos tienes: {cant_vehiculos}")
if cant_vehiculos > 0:
    print("tiene un vehiculo o mas")
elif cant_vehiculos >= 6:
    print("Tiene seis o mas vehiculos")
else:     
    print("Cantidad invalida, ingrese un numero entero positivo")

placa_auto = int(input("Digito y letra de la placa: "))
capacidad_de_carga = int(input("ingrese la cantidad de toneladas: "))