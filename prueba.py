faltan_productos = 'S'
total = 0
while faltan_productos == 'S':
    
    valor_unitario=eval(input("Ingrese el valor unitario del producto: "))
    tiene_iva = input("¿El producto tiene IVA? S/N")
    cantidad_productos=eval(input("Ingrese la cantidad de productos: "))
   
    if tiene_iva == 'S':
        print("IVA incluído")
        valor_unitario*=1.19
        subtotal=valor_unitario*cantidad_productos
    else:
        print("PRODUCTO SIN IVA")
        subtotal=valor_unitario*cantidad_productos
    
    total+= subtotal
    print(f"SUBTOTAL: {total}")
    faltan_productos = input("¿Faltan productos? S/N")
    if faltan_productos == 'N':
        print(f"TOTAL A COBRAR: {total}")
        break
        