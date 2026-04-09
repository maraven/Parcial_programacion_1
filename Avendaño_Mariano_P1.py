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
                    stock_valido = False
                    while not stock_valido:
                        stock = input(f"Ingrese el stock para {herramientas[i]}: ")
                        
                        #Validamos que el stock sea un número entero positivo o cero.
                        if stock.isdigit():
                            existencias[i] = int(stock)
                            stock_valido = True
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
                if buscar.isalpha():
                    #Buscamos la herramienta en la lista.
                    if buscar in herramientas:
                        #Extraemos el indice para mostrar el stock correspondiente.
                        indice= herramientas.index(buscar)
                        print(f"{herramientas[indice]}----- stock: {existencias[indice]}")
                        break
                    else:
                        print("-> Error: Herramienta no registrada.")
                print("-> Error: Dato no válido.")

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
            
            
            alta = input("Ingrese el nombre del nuevo producto: ").strip().capitalize()
            #Validamos que el nombre no este vacio, no sea un numero y no este repetido.
            if alta == "":
                print("-> Error: El nombre no puede estar vacío.")
            elif not alta.isalpha():
                print("-> Error: Dato no válido.")
            elif alta in herramientas:
                print("-> Error: La herramienta ya se encuentra registrada.")
            else:
                herramientas.append(alta)
                #existencias.append(0) #El nuevo producto se inicia con stock 0.
                #Se carga el stock.
                stock = input(f"Ingrese el stock para {alta}: ").strip()
                #Validamos que el stock sea un número entero positivo o cero.
                if stock.isdigit():
                    stock = int(stock)
                    existencias.append(stock) #Actualizamos el stock del nuevo producto.
                    print(f"-> Herramienta '{alta}' registrada con stock de {stock}.")
                else:
                    print("-> Error: El stock debe ser un número entero (0 o mayor).")
            

        case '7':
            print("\n--- 7. Actualización de Stock (Venta/Ingreso) ---")
            # TIP: Buscar herramienta. Preguntar si es Venta o Ingreso. 
            # Si es venta, validar que existencias[i] >= cantidad_venta antes de restar.
            print("Funcionalidad en construcción...")

        case '8':
            print("\n--- Cerrando el Sistema ---")
            # Cambiamos la variable de control para romper el bucle while
            sistema_activo = False

        case _:
            # Manejo de cualquier input que no sea del 1 al 8
            print("\n-> Opción inválida. Por favor, intente nuevamente.")
