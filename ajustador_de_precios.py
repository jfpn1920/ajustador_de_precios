ids = []
nombres = []
categorias = []
precios = []
cantidades = []
precios_anteriores = []
tipos_ajuste = []
valores_ajuste = []
fechas = []
estados = []
observaciones = []
historial_ids = []
historial_productos = []
historial_precios_anteriores = []
historial_precios_nuevos = []
historial_ajustes = []
historial_fechas = []
#-----------------------------------------#
#--|menu_principal_ajustador_de_precios|--#
#-----------------------------------------#
while True:
    print("menu principal ajustador de precios")
    print("1) registrar producto")
    print("2) editar producto")
    print("3) eliminar producto")
    print("4) buscar producto")
    print("5) ajustar precio")
    print("6) historial de precios")
    print("7) lista de productos")
    print("8) salir")
    opcion = input("seleccione una opción: ")
    #------------------------#
    #--|registrar_producto|--#
    #------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_producto = 1
        else:
            id_producto = ids[-1] + 1
        nombre = input("nombre del producto: ")
        categoria = input("categoría: ")
        try:
            precio = float(input("precio: "))
        except ValueError:
            precio = 0
        try:
            cantidad = int(input("cantidad: "))
        except ValueError:
            cantidad = 0
        fecha = input("fecha: ")
        observacion = input("observación: ")
        precios_anteriores.append(precio)
        tipos_ajuste.append("sin ajuste")
        valores_ajuste.append(0)
        estados.append("activo")
        ids.append(id_producto)
        nombres.append(nombre)
        categorias.append(categoria)
        precios.append(precio)
        cantidades.append(cantidad)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("producto registrado correctamente.")
        print("id:", id_producto)
        print("precio:", precio)
    #---------------------#
    #--|editar_producto|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("productos registrados")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{categorias[i]} | "
                    f"{precios[i]:.2f} | "
                    f"{cantidades[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id del producto: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("nombre:", nombres[posicion])
                print(
                    "categoría:",
                    categorias[posicion]
                )
                print(
                    "precio:",
                    precios[posicion]
                )
                print(
                    "cantidad:",
                    cantidades[posicion]
                )
                print(
                    "fecha:",
                    fechas[posicion]
                )
                print(
                    "observación:",
                    observaciones[posicion]
                )
                nombres[posicion] = input(
                    "nuevo nombre: "
                )
                categorias[posicion] = input(
                    "nueva categoría: "
                )
                try:
                    cantidades[posicion] = int(
                        input("nueva cantidad: ")
                    )
                except ValueError:
                    cantidades[posicion] = 0
                fechas[posicion] = input(
                    "nueva fecha: "
                )
                observaciones[posicion] = input(
                    "nueva observación: "
                )
                print(
                    "¿desea modificar también el precio?"
                )
                print("1) sí")
                print("2) no")
                modificar_precio = input(
                    "seleccione una opción: "
                )
                if modificar_precio == "1":
                    try:
                        nuevo_precio = float(
                            input("nuevo precio: ")
                        )
                    except ValueError:
                        nuevo_precio = precios[posicion]
                    precios_anteriores[posicion] = (
                        precios[posicion]
                    )
                    precios[posicion] = nuevo_precio
                    tipos_ajuste[posicion] = (
                        "modificación manual"
                    )
                    valores_ajuste[posicion] = (
                        nuevo_precio
                        - precios_anteriores[posicion]
                    )
                    if len(historial_ids) == 0:
                        id_historial = 1
                    else:
                        id_historial = (
                            historial_ids[-1] + 1
                        )
                    historial_ids.append(id_historial)
                    historial_productos.append(
                        nombres[posicion]
                    )
                    historial_precios_anteriores.append(
                        precios_anteriores[posicion]
                    )
                    historial_precios_nuevos.append(
                        nuevo_precio
                    )
                    historial_ajustes.append(
                        "modificación manual"
                    )
                    historial_fechas.append(
                        fechas[posicion]
                    )
                print(
                    "producto actualizado correctamente."
                )
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_producto|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("productos registrados")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{precios[i]:.2f}"
                )
            id_buscar = int(
                input("ingrese la id del producto: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print(
                    "producto:",
                    nombres[posicion]
                )
                print(
                    "precio:",
                    precios[posicion]
                )
                confirmacion = input(
                    "¿desea eliminar este producto? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    precios.pop(posicion)
                    cantidades.pop(posicion)
                    precios_anteriores.pop(posicion)
                    tipos_ajuste.pop(posicion)
                    valores_ajuste.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print(
                        "producto eliminado correctamente."
                    )
                else:
                    print(
                        "el producto no fue eliminado."
                    )
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_producto|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            id_buscar = int(
                input("ingrese la id del producto: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("información del producto")
                print("id:", ids[posicion])
                print(
                    "nombre:",
                    nombres[posicion]
                )
                print(
                    "categoría:",
                    categorias[posicion]
                )
                print(
                    "precio:",
                    precios[posicion]
                )
                print(
                    "cantidad:",
                    cantidades[posicion]
                )
                print(
                    "precio anterior:",
                    precios_anteriores[posicion]
                )
                print(
                    "tipo de ajuste:",
                    tipos_ajuste[posicion]
                )
                print(
                    "valor del ajuste:",
                    valores_ajuste[posicion]
                )
                print(
                    "fecha:",
                    fechas[posicion]
                )
                print(
                    "estado:",
                    estados[posicion]
                )
                print(
                    "observación:",
                    observaciones[posicion]
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|ajustar_precio|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("productos registrados")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{precios[i]:.2f}"
                )
            id_buscar = int(
                input("ingrese la id del producto: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                precio_actual = precios[posicion]
                print(
                    "producto:",
                    nombres[posicion]
                )
                print(
                    "precio actual:",
                    precio_actual
                )
                print("tipo de ajuste")
                print("1) aumentar porcentaje")
                print("2) disminuir porcentaje")
                print("3) aumentar valor")
                print("4) disminuir valor")
                print("5) establecer nuevo precio")
                tipo = input(
                    "seleccione una opción: "
                )
                nuevo_precio = precio_actual
                tipo_ajuste = "sin ajuste"
                valor_ajuste = 0
                if tipo == "1":
                    try:
                        porcentaje = float(
                            input(
                                "porcentaje de aumento: "
                            )
                        )
                    except ValueError:
                        porcentaje = 0
                    nuevo_precio = (
                        precio_actual
                        + (
                            precio_actual
                            * porcentaje
                            / 100
                        )
                    )
                    tipo_ajuste = (
                        "aumento por porcentaje"
                    )
                    valor_ajuste = porcentaje
                elif tipo == "2":
                    try:
                        porcentaje = float(
                            input(
                                "porcentaje de descuento: "
                            )
                        )
                    except ValueError:
                        porcentaje = 0
                    nuevo_precio = (
                        precio_actual
                        - (
                            precio_actual
                            * porcentaje
                            / 100
                        )
                    )
                    if nuevo_precio < 0:
                        nuevo_precio = 0
                    tipo_ajuste = (
                        "disminución por porcentaje"
                    )
                    valor_ajuste = porcentaje
                elif tipo == "3":
                    try:
                        valor = float(
                            input(
                                "valor del aumento: "
                            )
                        )
                    except ValueError:
                        valor = 0
                    nuevo_precio = (
                        precio_actual + valor
                    )
                    tipo_ajuste = "aumento por valor"
                    valor_ajuste = valor
                elif tipo == "4":
                    try:
                        valor = float(
                            input(
                                "valor de la disminución: "
                            )
                        )
                    except ValueError:
                        valor = 0
                    nuevo_precio = (
                        precio_actual - valor
                    )
                    if nuevo_precio < 0:
                        nuevo_precio = 0
                    tipo_ajuste = (
                        "disminución por valor"
                    )
                    valor_ajuste = valor
                elif tipo == "5":
                    try:
                        nuevo_precio = float(
                            input(
                                "nuevo precio: "
                            )
                        )
                    except ValueError:
                        nuevo_precio = precio_actual
                    if nuevo_precio < 0:
                        nuevo_precio = 0
                    tipo_ajuste = (
                        "nuevo precio"
                    )
                    valor_ajuste = nuevo_precio
                else:
                    print("opción no válida.")
                if tipo in ["1", "2", "3", "4", "5"]:
                    print("resultado del ajuste")
                    print(
                        "precio anterior:",
                        precio_actual
                    )
                    print(
                        "precio nuevo:",
                        round(nuevo_precio, 2)
                    )
                    print(
                        "tipo de ajuste:",
                        tipo_ajuste
                    )
                    confirmacion = input(
                        "¿desea aplicar el ajuste? (s/n): "
                    )
                    if confirmacion.upper() == "S":
                        precios_anteriores[posicion] = (
                            precio_actual
                        )
                        precios[posicion] = round(
                            nuevo_precio,
                            2
                        )
                        tipos_ajuste[posicion] = (
                            tipo_ajuste
                        )
                        valores_ajuste[posicion] = (
                            valor_ajuste
                        )
                        if len(historial_ids) == 0:
                            id_historial = 1
                        else:
                            id_historial = (
                                historial_ids[-1] + 1
                            )
                        historial_ids.append(
                            id_historial
                        )
                        historial_productos.append(
                            nombres[posicion]
                        )
                        historial_precios_anteriores.append(
                            precio_actual
                        )
                        historial_precios_nuevos.append(
                            round(nuevo_precio, 2)
                        )
                        historial_ajustes.append(
                            tipo_ajuste
                        )
                        historial_fechas.append(
                            fechas[posicion]
                        )
                        print(
                            "precio ajustado correctamente."
                        )
                        print(
                            "precio anterior:",
                            precio_actual
                        )
                        print(
                            "precio nuevo:",
                            precios[posicion]
                        )
                    else:
                        print(
                            "ajuste cancelado."
                        )
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|historial_de_precios|--#
    #--------------------------#
    elif opcion == "6":
        if len(historial_ids) == 0:
            print(
                "no existen ajustes registrados."
            )
        else:
            print("historial de precios")
            for i in range(
                len(historial_ids)
            ):
                print(
                    f"{historial_ids[i]} | "
                    f"{historial_productos[i]} | "
                    f"{historial_precios_anteriores[i]:.2f} "
                    f"-> "
                    f"{historial_precios_nuevos[i]:.2f} | "
                    f"{historial_ajustes[i]} | "
                    f"{historial_fechas[i]}"
                )
            print(
                "total de ajustes:",
                len(historial_ids)
            )
    #------------------------#
    #--|lista_de_productos|--#
    #------------------------#
    elif opcion == "7":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            precio_total = 0
            precio_mayor = precios[0]
            precio_menor = precios[0]
            producto_mayor = nombres[0]
            producto_menor = nombres[0]
            activos = 0
            print("lista de productos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{categorias[i]} | "
                    f"{precios[i]:.2f} | "
                    f"{cantidades[i]} | "
                    f"{estados[i]}"
                )
                precio_total += precios[i]
                if precios[i] > precio_mayor:
                    precio_mayor = precios[i]
                    producto_mayor = nombres[i]
                if precios[i] < precio_menor:
                    precio_menor = precios[i]
                    producto_menor = nombres[i]
                if estados[i] == "activo":
                    activos += 1
            promedio = precio_total / len(ids)
            print("estadísticas")
            print(
                "productos registrados:",
                len(ids)
            )
            print(
                "productos activos:",
                activos
            )
            print(
                "precio promedio:",
                round(promedio, 2)
            )
            print(
                "precio más alto:",
                producto_mayor,
                "-",
                precio_mayor
            )
            print(
                "precio más bajo:",
                producto_menor,
                "-",
                precio_menor
            )
            print(
                "ajustes realizados:",
                len(historial_ids)
            )
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "8":
        print(
            "gracias por utilizar el ajustador de precios."
        )
        break
    else:
        print("opción no válida.")