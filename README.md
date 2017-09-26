# Prueba Técnica - Programador (back-end)
La siguiente es una prueba para evaluar a los postulantes a programador **Backend-end**.

## INTRODUCCIÓN
Este repositorio contiene una serie de requerimientos de un Caso Práctico, que busca evaluar las capacidades técnicas del candidato con respecto a las principales funciones y responsabilidades que se requieren dentro del área de Desarrollo de Tecnología de _GCP Global_.

#### ¿Qué se busca evaluar?
Principalmente los siguientes aspectos:
* Creatividad para resolver los requerimientos,
* Calidad del código entregado (estructura y buenas prácticas),
* Eficiencia de los algoritmos entregados,
* Familiaridad con Frameworks y plataformas de desarrollo.

## IMPORTANTE
1. Recomendamos emplear un máximo de **3 (tres) horas** y enviar todo lo que puedas.
2. Se requiere de una **cuenta de GitHub** para realizar este ejercicio.
3. **Antes de comenzar a programar:**
    * Realizar un `Fork` de este repositorio (https://github.com/ORCAapplicants/backend-test).
    * Clonar el fork a su máquina local  `git clone git@github.com:USERNAME/FORKED-PROJECT.git`
    * Crear un `branch` en su cuenta de GitHub utilizando su nombre completo.
6. **Al finalizar**, existen 2 (dos) opciones para entregar su proyecto:
    * 1) Realizar un `Commit` de su proyecto, **enviar un `Pull Request` al branch con su NOMBRE**, y notificar a la siguiente dirección de correo electrónico  [developer@gcpglobal.com](mailto:developer@gcpglobal.com).
    * 2) Crear un archivo comprimido (_.zip_ o _.rar_) de su proyecto y enviar a la siguiente dirección de correo electrónico  [developer@gcpglobal.com](mailto:developer@gcpglobal.com).

## EJERCICIOS

### Ejercicio #1.
Escribir un simple programa que imprima en pantalla los primeros 100 números. Si un número es múltiplo de 3, se escribe “Fizz” en su lugar. Si el número es múltiplo de 5, se escribe “Buzz”. Si el número es múltiplo de ambos se escribe “FizzBuzz”.
* Escribe el algoritmo con base al problema planteado.
* Selecciona un Lenguaje de Programación de entre aquellos que figuran en tu CV y escribe el código.

###Ejercicio #2
Se tiene la clase InstanceGarbage con el método main. Indicar claramente las instrucciones en que se produce la creación de objetos y también las instrucciones que causan que un objeto sea elegible por el Garbage Collector al ejecutar el método main. 
```java
1	public class InstanceGarbage {
2		private static Integer metodo1(Integer[] a) {
3			a = new Integer[2];
4			a[0] = new Integer(1);
5			a[1] = new Integer(2);
6	
7			return a[0];
8		}
9	
10		public static void main(String[] args) {
11			Integer[] a = null;
12			Integer i = metodo1(a);
13	
14			do {
15				Integer j = new Integer(3);
16				i = j;
17			} while (false);
18			i = new Integer(4);
19		}
20	}
```

Para evitar confusión utilizar frases del tipo:
* "En la instrucción... se crea el objeto..."
* "Como consecuencia de la instrucción... el objeto... se convierte en basura"
* "Tras la ejecución de la instrucción... el objeto... se convierte en basura"

### Ejercicio #3.
Implementa el método: 
```java
public static ArrayList<Punto> leeArchivoPuntos(String nomArchivo) throws FileNotFoundException
```
que realiza la lectura de un archivo de texto que contiene un conjunto de puntos (uno por línea) y regresa esos puntos en un ArrayList.
El formato del archivo es el siguiente:
```
Punto         (3.45, -34.02 )
Punto  ( -2.3 ,3.0)   
Punto      (4.56,23.14   )
```
##### Consideraciones:
* El número de espacios entre la palabra "Punto" y el paréntesis abierto es variable (puede haber uno o más).
* Puede haber espacios entre el paréntesis abierto y el primer número, antes o después de la coma y antes del paréntesis cerrado.

El archivo puede contener errores de formato. Cuando se encuentre una línea con un error de formato se introducirá en el ArrayList un punto en el que sus coordenadas (x, y) tengan el máximo valor que es posible almacenar en un double. Después de encontrar una línea errónea el método no debe finalizar, sino que deberá continuar procesando las restantes líneas del archivo.

La clase `Punto` es:
```java
public class Punto {
	double x;
	double y;

	public Punto(double x, double y) {
		this.x = x;
		this.y = y;
	}
}
```

### Ejercicio #4.
Se desea administrar el acceso de vehículos a un estacionamiento de pago. El estacionamiento no se encuentra automatizado, por lo que existe un empleado encargado de registrar las entradas y salidas de vehículos.

Los vehículos se identifican por su número de placa. Cuando un vehículo entra en el estacionamiento el empleado registra su entrada y al salir registra su salida y, en algunos casos, cobra el importe correspondiente por el tiempo de estacionamiento.

El importe cobrado depende del tipo de vehículo:
* Los vehículos oficiales no pagan, pero se registran sus estancias para llevar el control.
(Una estancia consiste en una hora de entrada y una de salida)
* Los residentes pagan a final de mes a razón de MXN$0.05  el minuto. La aplicación irá acumulando el tiempo (en minutos) que han permanecido estacionados.
* Los no residentes pagan a la salida del estacionamiento a razón de MXN$0.5 por minuto.
Se prevé que en el futuro puedan incluirse nuevos tipos de vehículos, por lo que la aplicación desarrollada deberá ser fácilmente extensible en ese aspecto.

##### Casos de uso
![ Casos de uso](https://github.com/ORCAapplicants/backend-test/blob/master/img/backend-uc-01.png)

A continuación se describen los casos de uso. No se entra en detalles de la interacción entre el empleado y la aplicación (punto 1 de cada caso de uso), puesto que no va a ser tarea de este ejercicio desarrollar esa parte.

###### **Caso de uso "Registra entrada"**
1. El empleado elige la opción "registrar entrada" e introduce el número de placa del coche que entra.
2. La aplicación apunta la hora de entrada del vehículo.

###### **Caso de uso "Registra salida"**
1. El empleado elige la opción "registrar salida" e introduce el número de placa del coche que sale.
2. La aplicación realiza las acciones correspondientes al tipo de vehículo:
    * Oficial: asocia la estancia (hora de entrada y hora de salida) con el vehículo
    * Residente: suma la duración de la estancia al tiempo total acumulado
    * No residente: obtiene el importe a pagar

###### **Caso de uso "Da de alta vehículo oficial"**
1. El empleado elige la opción "dar de alta vehículo oficial" e introduce su número de placa.
2. La aplicación añade el vehículo a la lista de vehículos oficiales

###### **Caso de uso "Da de alta vehículo de residente"**
1. El empleado elige la opción "dar de alta vehículo de residente" e introduce su número de placa.
2. La aplicación añade el vehículo a la lista de vehículos de residentes.

###### **Caso de uso "Comienza mes"**
1. El empleado elige la opción "comienza mes".
2. La aplicación elimina las estancias registradas en los coches oficiales y pone a cero el tiempo estacionado por los vehículos de residentes.

###### **Caso de uso "Pagos de residentes"**
1. El empleado elige la opción "genera informe de pagos de residentes" e introduce el nombre del archivo en el que quiere generar el informe.
2. La aplicación genera un archivo que detalla el tiempo estacionado y el dinero a pagar por cada uno de los vehículos de residentes. El formato del archivo será el mostrado a continuación:

```
Núm. placa 	Tiempo estacionado (min.) 	Cantidad a pagar
S1234A 	    20134 				        1006.70
4567ABC	    4896				        244.80
... 		..... 				        .....
```
La aplicación contará con un programa principal basado en un menú que permitirá al empleado interactuar con la aplicación (dicho programa principal no forma parte de este ejercicio).

##### Persistencia de datos
La información de cada una de las estancias de los vehículos será almacenada en una base de datos. Debido a que el manejador de base de datos puede ser modificado en cualquier momento, se utilizará Hibernate como ORM.

##### Puntos que se deben desarrollar
* Diagrama de clases y diagrama de secuencia  de las partes encargadas de la aplicación.
* Aplicación para gestionar las estancias de los vehículos. Deberá incluir:
    * Código de las clases que permitan gestionar los vehículos con sus datos asociados (estancias, tiempo, etc.), las listas de vehículos registrados como oficiales y residentes, etc.
    * Mapeo de las clases para poder almacenar la información en la base de datos.
    * Clases para gestionar la persistencia de datos, incluida la configuración de conexión a la base de datos.

##### Consideraciones.
Para obtener la fecha y hora actual se utiliza la clase `Calendar`:
``` java
Calendar unaFecha; // para almacenar una fecha
unaFecha = Calendar.getInstance(); // obtiene la fecha actual
```
Para obtener intervalos de tiempos entre dos fechas suponer que se dispone del método:
```java
/** Obtiene la diferencia en minutos entre dos fechas
* @param inicial fecha inicial
* @param final fecha final
* @return diferencia final-inicial en minutos
*/
private static int difEnMinutos(Calendar inicial, Calendar final) {...}
```

