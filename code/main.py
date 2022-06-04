''' 
PRUEBA TECNICA BACK-END.
Problema: Parqueadero
David Santiago Rojo C. (dsrojo10@gmail.com)
'''

# librerias implementadas
import datetime
import time # para el tiempo actual

# Funciones
def calcularTiempo(placa):
    t1 = cars_init[placa]
    t2 = cars_close[placa]
    t = (t2 - t1)
    return t

# Diccionarios para almacenar los datos
cars_time = {} # Diccionario para el tiempo total de estancia de cada auto
cars_init = {} # Diccionario para la hora de llegada al parqueadero 
cars_close = {} # Diccionario para la hora de salida del parqueadero 
carsOF = [] # Vector para listar los autos oficiales
carsRSD = [] # Vector para listar los autos residentes

while True:
    #MENU
    print("\n------------PARQUEADERO------------\n")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Da de alta vehiculo OFICIAL")
    print("4. Da de alta vehiculo RESIDENTE")
    print("5. Comienza mes")
    print("6. Pagos residentes")
    print("7. SALIR (CERRAR SISTEMA)")
    print("8. Listar diccionarios: (prueba)")
    print("9. Restar tiempo")
    print("Seleccione una opcion:")
    aux = input()

    if(aux == '7' or aux == 7):
        break
    
    # REGISTRAR ENTRADA
    if(aux == '1' or aux == 1):
        print("Ingrese la placa del auto ingresado:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        cars_init[placa] = datetime.datetime.now() # Se almacena los datos de entrada del parqueadero
        print(cars_init) # Se muestra el diccionario con horas de entrada
        print("HORA DE ENTRADA:\n",cars_init) # Se muestra el diccionario con horas de ingreso

    # REGISTRAR SALIDA
    if(aux == '2' or aux == 2):
        print("Ingrese la placa del auto que sale:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        cars_close[placa] = datetime.datetime.now() # Se almacena los datos de salida del parqueadero
        print(cars_close) # Se muestra el diccionario con horas de salida
        # registrarTiempo(placa, cars_close)
        if(placa in carsOF):
            cars_time[placa] = calcularTiempo(str(placa))
        if(placa in carsRSD):
            cars_time[placa] = calcularTiempo(str(placa))
        else:
            deuda = calcularTiempo(placa)
            print("---------------------------------------")
            print("El tiempo que estuvo fue:")
            print(deuda) 
            print("---------------------------------------")
        # # print("\nEl auto ", placa, "debe pagar:", deuda*0.05, "MXN\n" )
        # # print("El auto ",placa," debe: ", deuda*0.05," MXN")

        
    # DAR DE ALTA VEHICULO OFICIAL
    if(aux == '3' or aux == 3):
        print("Ingrese la placa del auto a registrar:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        carsOF.append(placa)
        print(carsOF)
    
    # DAR DE ALTA VEHICULO OFICIAL
    if(aux == '4' or aux == 4):
        print("Ingrese la placa del auto a registrar:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        carsRSD.append(placa)
        print(carsRSD)
    
    # COMIENZA MES
    if(aux == '5' or aux == 5):
        # Se limpian todos los diccionarios que tengan tiempos almacenados
        cars_time.clear()
        cars_init.clear()
        cars_close.clear()

    # PAGOS RESIDENTES
    if(aux == '6' or aux == 6):
        print("PLACA:          TIEMPO(min):        DEUDA")
        for i in carsRSD:
            print(i, "       ",cars_time[i], "    $$$")
        
    # LISTAR TIEMPOS
    if(aux == '8' or aux == 8):
        print("Times:")
        print(cars_time)
        print("Times init:")
        print(cars_init)
        print("Times close:")
        print(cars_close)

    # CALCULAR TIEMPO DENTR DEL PARQUEADERO
    if(aux == '9' or aux == 9):
        print("Ingrese la placa del auto")
        placa = input()
        placa = placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        print(calcularTiempo(placa))





