package ejercicios.tres;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * 
 */

/**
 * @author croblesm
 *
 */
public class Ejercicio3 {

	public static ArrayList<Punto> leeArchivoPuntos(String nomArchivo) throws FileNotFoundException {
		String cadena;
		FileReader f = new FileReader(nomArchivo);
		BufferedReader b = new BufferedReader(f);
		ArrayList<Punto> listaPuntos = new ArrayList<Punto>();
		StringTokenizer elementos;
		Punto puntoSave;

		try {
			while ((cadena = b.readLine())!=null) {
				elementos = new StringTokenizer(cadena,"()");
				int count=0;
				if (elementos.countTokens()==1) {
					puntoSave = new Punto(Double.MAX_VALUE, Double.MAX_VALUE);
					listaPuntos.add(puntoSave);
				} else {
					while(elementos.hasMoreTokens()){
						count++;
						if (count == 2) {
							String [] campos = elementos.nextToken().split(",");
							try {
								puntoSave = new Punto(Double.parseDouble(campos[0].trim()), Double.parseDouble(campos[1]));
							} catch (NumberFormatException ex) {
								puntoSave = new Punto(Double.MAX_VALUE, Double.MAX_VALUE);
							}
							listaPuntos.add(puntoSave);
						} else {
							elementos.nextToken();
						}
					}
				}
				
			}
			b.close();
		} catch (IOException e) {

		}

		return listaPuntos;
	}
	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			ArrayList<Punto> listaFinal = leeArchivoPuntos("D://Puntos.txt");
			for (Punto punto : listaFinal) {
				System.out.println("Punto -> x="+punto.x+" y="+punto.y);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

}
