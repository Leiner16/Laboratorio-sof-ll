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