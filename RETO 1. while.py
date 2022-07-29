#Reto 1 mintic 
precio = 0
iva = 0.19
cantidad = 0
subtotal= 0
total = 0
contador = 0
faltan="S"
while faltan == "S":
    precio = float(input("Ingrese el valor unitario: "))
    p_iva = input("¿El producto cuenta con IVA?: ")
    cantidad = int(input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))
    if p_iva == "S":
        print("IVA incluído")
        valor = (precio*cantidad)*iva+(precio*cantidad)
        subtotal = valor
        total_parcial = subtotal + contador
        print(f"SUBTOTAL: ",total_parcial)
    elif p_iva == "N" :
        print("PRODUCTO SIN IVA")
        valor = (precio*cantidad)
        subtotal = valor
        total_parcial = subtotal + contador
        print(f"SUBTOTAL: ",total_parcial)
    else:
        break
    faltan=input("¿Faltan productos por cobrar? S/N: ")
    if faltan == "S":
        total = contador + subtotal
    elif faltan == "N":
        total = contador + subtotal
        print(f"TOTAL A COBRAR: ",total)
        break
    else:
        break
    contador = contador + subtotal

#segunda parte del reto

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    if semestre not in range(1, len(pensum) + 1):
        mensaje = "Ingrese un semestre válido"
    elif len(pensum[semestre - 1]) == 0:
        mensaje = "El semestre no tiene materias"
    else:
        if materia not in pensum[semestre - 1]:
            mensaje = "La materia no existe"
        else:
            pensum[semestre-1][materia]["créditos" ]=creditos
            pensum[semestre-1][materia]["nombre" ]= nombre
            mensaje="Modificada con éxito"
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje
d=pensum=[
    {"0123":{"nombre": "intro a la ing", "créditos": 2 },
    "4567":{"nombre": "inglés", "créditos": 1}},
    {},
    {}],
modificar_materia(d,"0123","nombre: intro a la ing y créditos 2,","hhhh",11111)

