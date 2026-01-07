public class Algoritimo {

	public static void main(String [] args){
		int numero = Integer.parseInt(args[0]);
		
		int [] lista = new int [11];
		
		for (int i = 0; i < lista.length; i++){
			lista[i] = i;
		}
	
		for (int i = 0; i < lista.length; i++){
		lista[i] = lista[i] * lista[i] * lista[i] * lista[i];
		}

		
		int baixo = 0;
		int alto = lista.length - 1;
		
		System.out.println("=======================================================================");
		for(int i = 0; i < lista.length; i++ ){
			System.out.print(" | " + lista[i]);
		}
		System.out.println(" | ");
		System.out.println("=======================================================================");
		
		while (baixo <= alto) {
			int medio = (baixo + alto) / 2;
			int chute = lista[medio];
			
			if (chute == numero) {
				System.out.printf("número: %d -> encontrado na pos %d", numero, medio);
				return;
			}
			
			if (chute < numero) {
				baixo = medio + 1;
			} else if (chute > numero) {
				alto = medio - 1;
			}
		}
		
		
		System.out.printf("Número %d inexistente na lista atual!", numero);
		return;
	
	}

}