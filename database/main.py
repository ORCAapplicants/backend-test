"""" 
BASE DE DATOS PARQUEADERO (Prueba tecnica de Backend)
David Santiago Rojo C.
"""

import sqlite3
import datetime
from autos import Auto
import autosDB

# Se crea la tabla
autosDB.crear_tabla_carros()


# Creamos 4 objetos de tipo Auto(placa, residente, oficial, tiempo).
carro1 = Auto('AAA111', '0', '0', 0)
carro2 = Auto('BBB222', '1', '0', 0)
carro3 = Auto('CCC333', '0', '1', 0)
carro4 = Auto('DDD444', '0', '0', 0)

# Se insertan los carros a la tabla.
autosDB.insetar_carro(carro1)
autosDB.insetar_carro(carro2)
autosDB.insetar_carro(carro3)
autosDB.insetar_carro(carro4)

# Seleccionamos uno en especifico por placa.
print(autosDB.selecionar_carro('AAA111'))

# Se muestran todos los valores alojados en la tabla.
autosDB.seleccionar_todos()

# Se eliminan dos autos de la tabla
autosDB.eliminar_carro('AAA111')
autosDB.eliminar_carro('BBB222')


# Se muestran todos los valores alojados en la tabla para verificar la eliminacion
autosDB.seleccionar_todos()

# Se cambia el estatus de algun auto (pasa a ser OFICIAL)
autosDB.actualizar_oficial("DDD444",1)

# Se muestran todos los valores alojados en la tabla para verificar la actualizacion
autosDB.seleccionar_todos()