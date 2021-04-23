import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class uri1256 {


	public static class No {

		private int numero;
		private No proximo;


		public No(int numero) {

			this.numero = numero;
			this.proximo = null;
		}


		public int getNumero() {
			return numero;
		}


		public void setNumero(int numero) {
			this.numero = numero;
		}


		public No getProximo() {
			return proximo;
		}


		public void setProximo(No proximo) {
			this.proximo = proximo;
		}


	}


	public static class Lista {

		private No primeiro;
		private No ultimo;


		public Lista() {

			this.primeiro = null;
			this.ultimo = null;
		}

		public void add(int numero) {

			No novo = new No(numero);

			if(primeiro == null) {

				primeiro = novo;
				ultimo = novo;

			} else {

				ultimo.setProximo(novo);
				ultimo = novo;
			}
		}

		public void  exibir() {

			No aux = primeiro; 

			while(aux!= null) {

				System.out.print(aux.getNumero() + " -> ");
				aux = aux.getProximo();

			}

			System.out.print("\\");
		}
	}

	public static class HashMap {

		private int tamanho;

		Lista [] vetor;

		public HashMap(int tamanho) {

			this.tamanho = tamanho;

			vetor = new Lista[tamanho];

			for(int i = 0; i < tamanho; i++) {


				vetor[i] = new Lista();

			}
		}

		public void add(int elemento) {

			int hashing = (elemento%tamanho);

			vetor[hashing].add(elemento);

		}

		public void exibir() {



			for(int i = 0; i < tamanho;i++) {

				if(vetor[i] != null && i < tamanho - 1) {

					
					System.out.print(i);
					System.out.print(" -> ");
					vetor[i].exibir();
					System.out.println();
					

				} else {
					
					System.out.print(i);
					System.out.print(" -> ");
					vetor[i].exibir();
				}
				

			}

		}
	}


	public static void main(String[] args) throws IOException {

		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);



		int tamanho;

		int hashqtd;


		int qtd = Integer.parseInt(in.readLine());

		for(int i = 0; i < qtd;i++) {

                        
                        
			String qtdNumero [] = new String [2];

			qtdNumero = in.readLine().split(" ");
                        


			HashMap hash = new HashMap(Integer.parseInt(qtdNumero[0])); // [0] tamanho do hashing
                        

			String numero[] = in.readLine().split(" ");



			for(int j = 0; j < Integer.parseInt(qtdNumero[1]);j++) { // [1] qtd de elementos do hashing



				hash.add(Integer.parseInt(numero[j]));

			}
                        
                        

                        hash.exibir();

                            

                          System.out.print("\n");
                          
                            if(i < qtd - 1){
                                System.out.println();
                            }

		}

        }	
}