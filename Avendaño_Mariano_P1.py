#herramientas[] pertenece a existencias[]

herramientas = []
existencias = []

#Variable de control para el bucle principal
sistema_activo = True
while sistema_activo:
    # Menú
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
    
    opcion = input("Ingrese el número de la opción deseada: ").strip() #se valida opcion en el match case
    
    match opcion:
        case '1':
            print("\n--- 1. Carga Inicial de Herramientas ---")
            cantidad = input("¿Cuántas herramientas distintas desea cargar?: ").strip()
            
            #Validación
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
                
                        #Se inicia la lista existencias en 0
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
                #Recorremos la lista de herramientas respetando el orden de ingreso
                for i in range(len(herramientas)):
                    stock_valido = False
                    while not stock_valido:
                        stock = input(f"Ingrese el stock para {herramientas[i]}: ")
                        
                        #Validamos que el stock sea un número entero positivo o cero
                        if stock.isdigit():
                            existencias[i] = int(stock)
                            stock_valido = True
                        else:
                            print("-> Error: El stock debe ser un número entero (0 o mayor).")
                print("-> Existencias actualizadas correctamente.")

        case '3':
            print("\n--- INVENTARIO ---")
            
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} ----- stock: {existencias[i]}")
            

        case '4':
            print("\n--- Consulta de Stock ---")
            buscar= input=(f"Ingrese producto: ").strip().capitalize()
            while True:
                if buscar.isalpha():
                    if buscar in herramientas:
                        indice= herramientas[buscar].index()
                        print(f"{herramientas[indice]}----- stock: {existencias[indice]}")
                        break
                    else:
                        print("herramienta no registrada.")
                else:
                    print("Error. Dato no válido.")

        case '5':
            print("\n--- PRODUCTOS SIN STOCK ---")
            sin_stock[]
            for i in range(len(existencias)):
              if existencias[i] == 0:
                sin_stock[i].append(herramientas[i])
            #se muestra listado sin stock
            for i in range(len(sin_stock)):
                print(sin_stock[i])
            # TIP: Recorrer 'existencias'. Si el valor es == 0, mostrar el nombre en 'herramientas' con ese mismo índice
            

        case '6':
            print("\n--- 6. Alta de Nuevo Producto ---")
            # TIP: Lógica muy similar a la opción 1, pero pidiendo solo un producto y su stock inicial
            print("Funcionalidad en construcción...")

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
