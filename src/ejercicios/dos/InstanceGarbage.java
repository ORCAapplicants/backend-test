package ejercicios.dos;

public class InstanceGarbage {
	private static Integer metodo1(Integer[] a) {
		a = new Integer[2];
		a[0] = new Integer(1);
		a[1] = new Integer(2);

		return a[0];
	}

	public static void main(String[] args) {
		Integer[] a = null;
		Integer i = metodo1(a);

		do {
			Integer j = new Integer(3);
			i = j;
		} while (false);
		i = new Integer(4);
	}
}