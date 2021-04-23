

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;




public class uri1195 {



	public static void main(String[] args) throws IOException {

		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		
		int qtd = Integer.parseInt(in.readLine());
		
		int z = 1;
		
		Arvore[] arvore = new Arvore[qtd];
		
		for(int i = 0; i < qtd;i++) {
			
			int qtd2 = Integer.parseInt(in.readLine());
			
			String numero [] = new String [qtd2];
			
			arvore[i] = new Arvore();
			
			numero = in.readLine().split(" ");
			
			for(int j = 0; j < qtd2;j++) {
				
				
				arvore[i].adicionar(Integer.parseInt(numero[j]));
			}
			
		}
		
		for(int j = 0; j < qtd;j++) {
			
			System.out.println("Case " + z + ":");
			
			System.out.print("Pre.:");
			arvore[j].PreOrdem();
			System.out.println(arvore[j].getA());
			System.out.print("In..:");
			
			
			arvore[j].EmOrdem();
			System.out.println(arvore[j].getB());
			System.out.print("Post:");
			arvore[j].PosOrdem();
			System.out.println(arvore[j].getC());
			
		
			System.out.println("");
			
			
			z++;
		}
 
	}


public static class No {

	private int numero;
	private No direita;
	private No esquerda;
	
	public No(int numero) {
		
		this.numero = numero;
		direita = null;
		esquerda = null;
		
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public No getDireita() {
		return direita;
	}

	public void setDireita(No direita) {
		this.direita = direita;
	}

	public No getEsquerda() {
		return esquerda;
	}

	public void setEsquerda(No esquerda) {
		this.esquerda = esquerda;
	}
	
	
}



public static class Arvore {

	private No raiz;
	private String a = "";
	private String b = "";
	private String c = "";

	public Arvore() {

		raiz = null;
	}

	public void adicionar(No n,int valor) {

		No novo = new No(valor);

		if(n.getNumero() == valor) {

			

		} else if(valor < n.getNumero()) {

			if(n.getEsquerda() == null) {

				n.setEsquerda(novo);

			} else {

				adicionar(n.getEsquerda(), valor);

			}

		} else if(valor > n.getNumero()) {

			if(n.getDireita() == null) {

				n.setDireita(novo);

			} else {

				adicionar(n.getDireita(),valor);
			}
		}

	}

	public void adicionar(int valor) {

		No novo = new No(valor);

		if(raiz == null) {

			raiz = novo;

		} else {

			adicionar(raiz,valor);
		}
	}

	public void PreOrdem(No n) {

		a+=  " " + n.getNumero();

		if(n.getEsquerda() != null) {

			PreOrdem(n.getEsquerda());

		}

		if(n.getDireita() != null) {

			PreOrdem(n.getDireita());
		}
	}

	public void EmOrdem(No n) {


		if(n.getEsquerda() != null) {

			EmOrdem(n.getEsquerda());

		}
		
		b+= " " + n.getNumero();

		if(n.getDireita() != null) {

			EmOrdem(n.getDireita());
		}
	}
	
	public void PosOrdem(No n) {


		if(n.getEsquerda() != null) {

			PosOrdem(n.getEsquerda());

		}
		

		if(n.getDireita() != null) {

			PosOrdem(n.getDireita());
		}
		
		c+= " " + n.getNumero();
	}
	
	public void PreOrdem() {
		
		PreOrdem(raiz);
	}
	
	public void EmOrdem() {
		
		EmOrdem(raiz);
		
	}
	
	public void PosOrdem() {
		
		PosOrdem(raiz);
	}

	public No getRaiz() {
		return raiz;
	}

	public void setRaiz(No raiz) {
		this.raiz = raiz;
	}

	public String getA() {
		return a;
	}

	public void setA(String a) {
		this.a = a;
	}

	public String getB() {
		return b;
	}

	public void setB(String b) {
		this.b = b;
	}

	public String getC() {
		return c;
	}

	public void setC(String c) {
		this.c = c;
	}
	
	
}

	}

