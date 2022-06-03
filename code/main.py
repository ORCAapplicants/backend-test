''' 
PRUEBA TECNICA BACK-END.
Problema: Parqueadero
David Santiago Rojo C. (dsrojo10@gmail.com)
'''

# librerias implementadas
import time # para el tiempo actual

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
    print("Seleccione una opcion:")
    aux = input()

    if(aux == '7' or aux == 7):
        break

    # REGISTRAR ENTRADA
    if(aux == '1' or aux == 1):
        print("Ingrese la placa del auto ingresado:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        # print(placa)
        tiempoInicial = time.ctime() # Se toma el tiempo actual
        tiempoInicial = tiempoInicial.split() # Se separan los datos de la fecha
        cars_init[placa] = tiempoInicial[3] # Se almacena los datos de entrada al parqueadero
        print("HORA DE ENTRADA:\n",cars_init) # Se muestra el diccionario con horas de ingreso

    # REGISTRAR SALIDA
    if(aux == '2' or aux == 2):
        print("Ingrese la placa del auto que sale:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        tiempoFinal = time.ctime() # Se toma el tiempo actual
        tiempoFinal = tiempoFinal.split() # Se separan los datos de la fecha
        cars_close[placa] = tiempoFinal[3] # Se almacena los datos de salida del parqueadero
        print(cars_close) # Se muestra el diccionario con horas de salida
        
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
    # if(aux == '6' or aux == 6):
        


