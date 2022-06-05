''' 
PRUEBA TECNICA BACK-END.
Problema: Parqueadero
David Santiago Rojo C. (dsrojo10@gmail.com)
'''

# librerias implementadas
# import os
import datetime
import sqlite3
import datetime
from autos import Auto
import autosDB

# Funciones
def calcularTiempo(placa):
    t1 = cars_init[placa]
    t2 = cars_close[placa]
    t = (t2 - t1)
    return t

def calcularMinutos(placa):
    t1 = cars_init[placa]
    t2 = cars_close[placa]
    t = (t2 - t1)
    minutes = t.total_seconds() / 60
    minutes = round(minutes,2)
    return minutes

"""" ------------ BASE DE DATOS ------------------- """
# Se crea la tabla
autosDB.crear_tabla_carros()
conn = sqlite3.connect('parqueadero.db')
c = conn.cursor()
print("La conexion con la base de datos fue exitosa!\n")

# # Creamos 4 objetos de tipo Auto(placa, residente, oficial, tiempo).
# carro1 = Auto('AAA111', '0', '0', 0)
# carro2 = Auto('BBB222', '1', '0', 0)
# carro3 = Auto('CCC333', '0', '1', 0)
# carro4 = Auto('DDD444', '0', '0', 0)

# # Se insertan los carros a la tabla.
# autosDB.insetar_carro(carro1)
# autosDB.insetar_carro(carro2)
# autosDB.insetar_carro(carro3)
# autosDB.insetar_carro(carro4)

# # Seleccionamos uno en especifico por placa.
# print(autosDB.selecionar_carro('AAA111'))

# # Se muestran todos los valores alojados en la tabla.
# autosDB.seleccionar_todos()

""" ----------------------------------------------  """

# Diccionarios para almacenar los datos
cars_time = {} # Diccionario para el tiempo total de estancia de cada auto
cars_init = {} # Diccionario para la hora de llegada al parqueadero 
cars_close = {} # Diccionario para la hora de salida del parqueadero 
carsOF = [] # Vector para listar los autos oficiales
carsRSD = [] # Vector para listar los autos residentes

"""" CARGAR DATOS DE LA BD A LOS VECTORES """
# Se cambia el estatus de oficial a no oficial
aux = autosDB.seleccionar_por_estatus("oficial")
for i in range(0, len(aux)):
    carsOF.append(aux[i][0])

# Se reinicia el tiempo de parqueo de residentes
aux = autosDB.seleccionar_por_estatus("residente")
for i in range(0, len(aux)):
    carsRSD.append(aux[i][0])
""" ------------------------------------- """

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

    # REGISTRAR ENTRADA
    if(aux == '1' or aux == 1):
        print("Ingrese la placa del auto ingresado:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        cars_init[placa] = datetime.datetime.now() # Se almacena los datos de entrada del parqueadero
        # cars_time[placa] = (datetime.datetime.now() - datetime.datetime.now()) # Se inicializa el tiempo en 0:00:00
        if(len(autosDB.selecionar_carro(placa)) == 0):
            autosDB.insetar_carro(Auto(placa, '0', '0', 0)) # En caso de que el carro nunca haya sido parqueado, se agrega a la BD
        print(cars_init) # Se muestra el diccionario con horas de entrada
        print("HORA DE ENTRADA:\n",cars_init) # Se muestra el diccionario con horas de ingreso

    # REGISTRAR SALIDA
    if(aux == '2' or aux == 2):
        print("Ingrese la placa del auto que sale:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        cars_close[placa] = datetime.datetime.now() # Se almacena los datos de salida del parqueadero
        print(cars_close) # Se muestra el diccionario con horas de salida

        if(placa in carsOF):
            print("OFICIAAAAAAAAAAL.")
            cars_time[placa] = calcularTiempo(str(placa)) # se almacena el tiempo que estuvo
            minutes = calcularMinutos(placa)
            autosDB.actualizar_tiempo(placa, minutes)
        if(placa in carsRSD):
            cars_time[placa] = calcularMinutos(str(placa)) # se almacena el tiempo que estuvo
            minutes = calcularMinutos(placa)
            autosDB.actualizar_tiempo(placa, minutes)
            print("RESIDENTESSSSSS.")
        if(placa not in carsOF and placa not in carsRSD):
            minutos = calcularMinutos(placa)
            # minutos = deuda.total_seconds / 60
            # minutos = round(minutos, 2)
            print("---------------------------------------")
            print("El tiempo que estuvo fue:")
            print(minutos) 
            print("El pago es:")
            print(minutos*0.5," MXN") 
            print("---------------------------------------")
            print("XXXXXXXXXXXXXXXXX")
        
    # DAR DE ALTA VEHICULO OFICIAL
    if(aux == '3' or aux == 3):
        print("Ingrese la placa del auto a registrar:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        if(placa not in carsOF):
            carsOF.append(placa)    
        autosDB.actualizar_oficial(placa, '1') # se actualiza el estatus en la base de datos a carro oficial
        print(carsOF)
    
    # DAR DE ALTA VEHICULO OFICIAL
    if(aux == '4' or aux == 4):
        print("Ingrese la placa del auto a registrar:") # Se solicita la placa
        placa=input() # Se recibe el dato por consola
        placa=placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        if(placa not in carsRSD):
            carsRSD.append(placa)
        autosDB.actualizar_residente(placa, '1') # se actualiza el estatus en la base de datos a carro residente
        print(carsRSD)
    
    # COMIENZA MES
    if(aux == '5' or aux == 5):
        # Se limpian todos los diccionarios que tengan tiempos almacenados
        cars_time.clear()
        cars_init.clear()
        cars_close.clear()

        # Se cambia el estatus de oficial a no oficial
        aux = autosDB.seleccionar_por_estatus("oficial")
        for i in range(0, len(aux)):
            autosDB.actualizar_oficial(aux[i][0], '0')
        
        # Se reinicia el tiempo de parqueo de residentes
        aux = autosDB.seleccionar_por_estatus("residente")
        for i in range(0, len(aux)):
            autosDB.actualizar_tiempo(aux[i][0], 0)

    # PAGOS RESIDENTES
    if(aux == '6' or aux == 6):
        print("Ingrese el nombre para el archivo de cuenta residentes:")
        nomArchivo = input()
        nomArchivo = nomArchivo+".txt"

        # Seleccionamos todos los residentes
        c.execute("SELECT * FROM tiempos_mes WHERE residente=?", (1,))
        carros = c.fetchall()
        print(carros)

        file = open(nomArchivo, "w")
        # file.write("PLACA:          TIEMPO(min):        DEUDA" + os.linesep)
        file.write("PLACA:      TIEMPO(min):      DEUDA:\n")
        # print("PLACA:          TIEMPO(min):        DEUDA")
        # for i in carsRSD:
        #     if(i in cars_time):
        #         contenido = i+ "       " + str(cars_time[i]) + "        " + str(cars_time[i]*0.05) + " MXN."
        #         print(i, "       ",cars_time[i], "        ", str(cars_time[i]*0.05), " MXN.")
        #         file.write(contenido + os.linesep)
        # file.close()

        for i in carros:
                contenido = i[0]+ "            " + str(i[3]) + "        " + str(i[3]*0.05) + " MXN.\n"
                # print(i, "       ",cars_time[i], "        ", str(cars_time[i]*0.05), " MXN.")
                # file.write(contenido + os.linesep)
                file.write(contenido)
        file.close()
        
    if(aux == '7' or aux == 7):
        break

    # LISTAR TIEMPOS
    if(aux == '8' or aux == 8):
        print("Times:")
        print(cars_time)
        print("Times init:")
        print(cars_init)
        print("Times close:")
        print(cars_close)
        print(autosDB.seleccionar_todos())

    # CALCULAR TIEMPO DENTRO DEL PARQUEADERO
    if(aux == '9' or aux == 9):
        print("Ingrese la placa del auto")
        placa = input()
        placa = placa.upper() # Se convierte a MAYUS para mantener coherencia entre datos
        print(calcularTiempo(placa))




