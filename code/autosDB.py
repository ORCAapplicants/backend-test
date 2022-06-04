import sqlite3

def crear_tabla_carros(): # Se crea la tabla de carros (placa, oficial(si o no), residente(si o no), tiempo(en min))
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tiempos_mes(
                placa TEXT PRIMARY KEY,
                oficial BIT,
                residente BIT,
                tiempo SMALLINT NOT NULL)""")
    conn.close()

def insetar_carro(car): # Se inserta un objeto(car) de tipo (Auto) a la tabla
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("INSERT INTO tiempos_mes VALUES (?,?,?,?)",
        (car.placa, car.oficial, car.residente, car.tiempo))
    conn.commit()
    conn.close()

def selecionar_carro(placa): # Se hace busqueda en la tabla con los metodos FROM y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tiempos_mes WHERE placa=?", (placa,))
    carro = c.fetchall()
    conn.close()
    return carro

def actualizar_tiempo(placa, tiempo): # Se actualiza un dato en la tabla con los metodos SET y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("UPDATE tiempos_mes SET tiempo=? WHERE placa=?",
                (tiempo, placa))
    conn.commit()
    conn.close()

def actualizar_oficial(placa, flag): # Se actualiza un dato en la tabla con los metodos SET y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("UPDATE tiempos_mes SET oficial=? WHERE placa=?",
                (flag, placa))
    conn.commit()
    conn.close()

def actualizar_residente(placa, flag): # Se actualiza un dato en la tabla con los metodos SET y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("UPDATE tiempos_mes SET residente=? WHERE placa=?",
                (flag, placa))
    conn.commit()
    conn.close()

def eliminar_carro(placa): # Se elimina un elemento de la tabla con su placa, se usan los metodos DELETE y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("DELETE from tiempos_mes WHERE placa=?", (placa,))
    conn.commit()
    conn.close()

def eliminar_tabla(): # Se elimina la tabla, se usan los metodos DELETE y WHERE
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("DELETE * FROM tiempos_mes")
    conn.commit()
    conn.close()

def seleccionar_todos(): # Se muestra el contenido total de la tabla, se usan los metodos SELECT y FROM
    conn = sqlite3.connect('parqueadero.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tiempos_mes")
    print(c.fetchall())
    conn.close()