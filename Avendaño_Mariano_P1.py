#herramientas[] pertenece a existencias[].

herramientas = []
existencias = []

#Variable de control para el bucle principal.
sistema_activo = True
while sistema_activo:
    # Menú.
    print("\n" + "="*45)
    print("FERRETERÍA - SISTEMA DE CONTROL DE INVENTARIO")
    print("="*45)
    print("1. Carga Inicial de Herramientas")
    print("2. Carga de Existencias")
    print("3. Visualización de Inventario")
    print("4. Consulta de Stock")
    print("5. Reporte de Agotados")
    print("6. Alta de Nuevo Producto")
    print("7. Actualización de Stock (Venta/Ingreso)")
    print("8. Salir")
    print("="*45)
    
    opcion = input("Ingrese el número de la opción deseada: ").strip() #se valida opcion en el match case.
    
    match opcion:
        case '1':
            print("\n--- Carga Inicial de Herramientas ---")
            cantidad = input("¿Cuántas herramientas distintas desea cargar?: ").strip()
            
            #Validación.
            if cantidad.isdigit() and int(cantidad) > 0:
                cantidad = int(cantidad)
                cargadas = 0
                
                #Usamos while para volver a pedir si hay error (vacío, duplicado o si carga un numero como nombre)
                #se utiliza el while con contador de cargadas, para que se carguen la cantidad de herramientas necesarias.
                while cargadas < cantidad:
                    nombre = input(f"Ingrese el nombre de la herramienta {cargadas + 1}: ").strip().capitalize()
                    
                    if nombre == "":
                        print("-> Error: El nombre no puede estar vacío.")
                    elif  not nombre.isalpha():
                        print("-> Error: Dato no válido.")
                    elif nombre in herramientas:
                        print("-> Error: La herramienta ya se encuentra registrada.")
                    else:
                        herramientas.append(nombre)
                
                        #Se inicia la lista existencias en 0.
                        existencias.append(0) 
                        cargadas += 1 
                print("-> Carga inicial completada con éxito.")
            else:
                print("-> Error: Debe ingresar un número entero mayor a 0.")

        case '2':
            print("\n--- STOCK ---")
            #Se inicia la carga siempre que la lista de herramientas este cargada.
            if len(herramientas) == 0:
                print("-> Error: No hay herramientas registradas. Ejecute la opción 1 primero.")
            else:
                #Recorremos la lista de herramientas respetando el orden de ingreso.
                for i in range(len(herramientas)):
                    while True:
                        stock = input(f"Ingrese el stock para {herramientas[i]}: ")
                        #Validamos que el stock sea un número entero positivo o cero.
                        if stock.isdigit():
                            existencias[i] = int(stock)
                            
                            break
                        else:
                            print("-> Error: El stock debe ser un número entero (0 o mayor).")
                print("-> Existencias actualizadas correctamente.")

        case '3':
            print("\n--- INVENTARIO ---")
            #Se recorre la lista de herramientas y existencias para mostrar el inventario completo.
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} ----- stock: {existencias[i]}")
            

        case '4':
            print("\n--- Consulta de Stock ---")
            while True:
                buscar = input(f"Ingrese producto: ").strip().capitalize()
                #Se valida que el dato sean letras.
                if not buscar.isalpha():
                    print("-> Error: Dato no válido.")
                    break
                else:
                    #Buscamos la herramienta en la lista.
                    for i in range(len(herramientas)):
                        if herramientas[i] == buscar:
                            print(f"{herramientas[i]} ----- stock: {existencias[i]}") 
                        else:
                            print("-> Error: Herramienta no registrada.")
                    break    

        case '5':
            print("\n--- PRODUCTOS SIN STOCK ---")
            sin_stock = []
            #Se recorre la lista de existencias y se crea otra lista con las herramientas con stock 0.
            for i in range(len(existencias)):
                if existencias[i] == 0:    
                    sin_stock.append(herramientas[i])
            #Si no hay productos con stock 0 se envia mensaje.
            if sin_stock == []:
                print(f"-> No hay productos sin stock.")
            for i in range(len(sin_stock)):
                print(f"{sin_stock[i]} ----- stock: 0")
                

        case '6':
            print("\n--- Alta de Nuevo Producto ---")
            alta = input(f"Ingrese el nombre del nuevo producto: ").strip().capitalize()
            #Validamos que el nombre no este vacio, no sea un numero y no este repetido.
            repetido = False
            for i in range(len(herramientas)):
                if alta == herramientas[i]:
                    print(f"-> Error: La herramienta ya se encuentra registrada.")
                    repetido = True
                    break
            if repetido == True:
                continue
            if alta == "":
                print(f"-> Error: El nombre no puede estar vacío.")
            elif not alta.isalpha():
                print(f"-> Error: Dato no válido.")
            #elif alta in herramientas:
            #    print(f"-> Error: La herramienta ya se encuentra registrada.")
            else:
                #se pide primero el stock para evitar que se agregue una herramienta sin stock.
                stock = input(f"Ingrese el stock para {alta}: ").strip()
                if stock.isdigit():
                    stock = int(stock)
                    #Actualizamos las listas.
                    herramientas.append(alta)
                    existencias.append(stock)
                    print(f"-> Herramienta '{alta}' registrada con stock de {stock}.")
                else:
                    print(f"-> Error: El stock debe ser un número entero (0 o mayor).")
            

        case '7':
            print("\n--- Actualización de Stock (Venta/Ingreso) ---")
            #Se pregunta si es Venta o Ingreso.

            opcion= input(f"Venta (V) o Ingreso (I): ").strip().upper()
            #Venta
            if opcion == 'V':
                while True:
                    ingreso_venta = input(f"Ingrese producto: ").strip().capitalize()
                    if not ingreso_venta.isalpha():
                        print(f"-> Error: Dato no válido.")
                        break

                    no_encontrado = False
                    for i in range(len(herramientas)):
                        if ingreso_venta != herramientas[i]:
                            no_encontrado = True
                            
                    if no_encontrado == True:
                        print(f"-> Error: El producto no esta en el catalogo.")
                        break
                    
                    #elif ingreso_venta not in herramientas:
                    #    print("-> Error: Herramienta no esta en el catalogo.")
                    else:
                        indice = herramientas.index(ingreso_venta)
                        venta = input(f"Ingrese cantidad a vender: ").strip()
                        if not venta.isdigit():
                            print(f"-> Error: La cantidad a vender debe ser un número entero mayor a 0.")
                        #Se verifica que la cantidad a vender no sea mayor al stock actual.
                        elif existencias[indice] >= int(venta):
                            existencias[indice] -= int(venta)
                            print(f"-> Venta realizada. Stock actualizado de {herramientas[indice]}: {existencias[indice]}")
                            break
                        else:
                            print(f"-> Error: Stock insuficiente. Stock actual de {herramientas[indice]}: {existencias[indice]}")
            #Ingreso
            elif opcion == 'I':
                while True:
                    ingreso = input(f"Ingresar nombre de producto: ").strip().capitalize()
                    if not ingreso.isalpha():
                        print(f"-> Error: Dato no válido.")
                        break
                    no_encontrado = False
                    #Se recorre la lista de herramientas para verificar si el producto a ingresar esta registrado o no.
                    for i in range(len(herramientas)):
                        if ingreso != herramientas[i]:
                            no_encontrado = True
                    if no_encontrado == True:
                        print(f"-> Error: El producto no esta en el catalogo.")
                        break
                    indice = herramientas.index(ingreso)
                    ingreso_stock = input(f"Ingrese nuevas existencias: ").strip()
                    #Se valida stock actualizado
                    if not ingreso_stock.isdigit():
                        print(f"-> Error: dato no válido.")
                    else:
                        ingreso_stock= int(ingreso_stock)
                        existencias[indice] += ingreso_stock
                        print(f"-> Stock actualizado de {herramientas[indice]}: {existencias[indice]}")
                    break   
            else:
                print(f"-> Error: debe ingresar 'V' o 'I'" )

        case '8':
            print("\n--- Cerrando el Sistema ---")
            # Cambiamos la variable de control para romper el bucle while
            sistema_activo = False

        case _:
            # Manejo de cualquier input que no sea del 1 al 8
            print("\n-> Opción inválida. Por favor, intente nuevamente.")
