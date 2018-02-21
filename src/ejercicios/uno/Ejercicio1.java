package ejercicios.uno;

/**
 * 
 */

/**
 * @author croblesm
 *
 */
public class Ejercicio1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		int multiplo3=3, multiplo5=5;

		for (int num=1; num<=100; num++) {
			if ((num%multiplo3)==0 && (num%multiplo5)==0) {
				System.out.println("FizzBuzz");
			} else if ((num%multiplo3)==0) {
				System.out.println("Fizz");
			} else if ((num%multiplo5)==0) {
				System.out.println("Buzz");
			} else {
				System.out.println(num);
			}
		}

	}

}
