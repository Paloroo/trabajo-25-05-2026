#             0       1         2       3        4         5          6
colores = ["rojo", "verde", "negro", "azul", "amarillo", "rosa", "violeta"]
colores.sort()
Busqueda = input("Ingrese un color: ").strip().lower()

valor_encontrado = False

for indice,color in enumerate(colores):
    if color == Busqueda:
        print(f"{indice+1} - color es: {color}")
        valor_encontrado = True
        break     
if not valor_encontrado:
    print("El valor no fue encontrado")

print("=======================================================================================================================")
# LISTAS CON PYTHON 

listado = ["rojo", "verde","negro", "violeta", "azul", "amarillo", "rosa"]
listado.append(0.1)

for elemento in listado:
    print(elemento)
#        INSERTACIONES
minilistado = ["rojo", "violeta", "negro", "azul", "verde", "amarillo", "rosa"]
minilistado.insert(4,"F.E")

for elemento in minilistado:
    print(elemento)
    print("=======================================================================================================================")

# ELIMINAR        1       2         3
    colores = ["rojo", "verde", "violeta"]
    colores.sort()
validar_color = False
while not validar_color:
    try:
        color_a_eliminar = input("Ingrese un color: ").strip().lower()
    except ValueError:
        print("Color ingresado erroneamente, intente nuevamente")
    else:
        validar_color = True
        print("=======================================================================================================================")

try:
    colores.remove(color_a_eliminar)
except ValueError:
    print("Color no encontrado, intente nuevamente")
else:
    for indice,color in enumerate(colores):
        print(f"{indice+1}° El color es: {color}")      
        print("=======================================================================================================================")             

        #outro
ciudades = {
    "chile":"santiago",
    "uruguay":"buenos aires",
    "brasil":"brasilia",
    "paraguay":"asunción",
    "ecuador":"quito",
    "colombia":"bogota",
    "bolivia":"sucre",
    "venezuela":"caracas",
    "peru":"lima"
}

print(ciudades["chile"])

for pais,ciudades in ciudades.items():
    print(f"{ciudades.title()} esta en: {pais.title()}")