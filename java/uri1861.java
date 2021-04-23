import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;




public class uri1861 {
	
	public static void main(String[] args) throws IOException {


		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);

		String pessoa [] = new String [2];

		Arvore arvore = new Arvore();

		LinkedList<String> assasinado = new LinkedList<String>();

	
		String string;

		while(in.ready()) {

			string = in.readLine();


			pessoa = string.split(" ");

			

			arvore.adicionar(pessoa[0]);
	

			assasinado.add(pessoa[1]);
		}
		
	
		for(String i: assasinado) {

			arvore.remover(i);
		}

       


		System.out.println("HALL OF MURDERERS");

		arvore.EmOrdem();
		


	}
	


public static class No {

	private String nome;
	private No esquerdo;
	private No direito;
	private int kill;
	private boolean remove;
	
	public No(String nome) {
		
		this.nome = nome;
		esquerdo = null;
		direito = null;
		kill = 1;
	}
	
	public boolean remover(String nome,No pai) {
		
		 if( nome.compareTo(this.nome) < 0) {
			
			if(esquerdo != null) 
				
				return esquerdo.remover(nome, this);
				
			 else 
				
				return false;
			
			
		} else if(nome.compareTo(this.nome) > 0) {
			
			if(direito != null) 
				
				return direito.remover(nome, this);
				
			 else 
				
				return false;
				
			} else {
			
			if(esquerdo != null && direito!= null) {
				
				No aux = direito.minValue();
				
				if(aux == null) {
					
					this.remove = true;
					
				} else {
					
					nome = aux.getNome();
					kill = aux.getKill();
				}
				
				
				direito.remover(this.nome,this);
		
				
			} else if(pai.esquerdo == this) {
				
				pai.esquerdo =((esquerdo!= null)?esquerdo:direito);
				
			} else if(pai.direito == this) {
				
				pai.direito =((esquerdo!= null)?esquerdo:direito);
			}
			
			return true;
		  }
		}
	
	
	 public No minValue() {

         if (esquerdo == null)

               return esquerdo;

         else

               return esquerdo.minValue();

   }
	 

	 



	public int getKill() {
		return kill;
	}

	public void setKill(int kill) {
		this.kill = kill;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public No getEsquerdo() {
		return esquerdo;
	}

	public void setEsquerdo(No esquerdo) {
		this.esquerdo = esquerdo;
	}

	public No getDireito() {
		return direito;
	}

	public void setDireito(No direito) {
		this.direito = direito;
	}

	public boolean getRemove() {
		return remove;
	}

	public void setRemove(boolean remove) {
		this.remove = remove;
	}


	
	
}



public static class Arvore {

	private No raiz;


	public Arvore() {

		raiz = null;

	}

	public void adicionar(No n,String nome) {

		No novo = new No(nome);
		
		if(nome.compareTo(n.getNome()) == 0) {
			
			n.setKill(n.getKill()+ 1);
			
			
		} else if(nome.compareTo(n.getNome()) < 0) {

			if(n.getEsquerdo() == null) {

				n.setEsquerdo(novo);
			

			} else {

				 adicionar(n.getEsquerdo(),nome);

			} 

		}	else if(nome.compareTo(n.getNome()) > 0) {

			   if(n.getDireito() == null) {
                
				   n.setDireito(novo);

			} else {
				
				 adicionar(n.getDireito(), nome);
			}
		}
		
		
	}


	public void adicionar(String nome) {

		No novo = new No(nome);

		if(raiz == null) {

			raiz = novo;

		} else {

			adicionar(raiz,nome);
		}
	}

	public boolean buscar(No n,String nome) {

		if(nome.compareTo(n.getNome()) == 0) {

        
			return true;

		} else if( nome.compareTo(n.getNome()) < 0) {

			if(n.getEsquerdo() == null) {

				return false;

			} else {

				return buscar(n.getEsquerdo(),nome);
			}

		} else if( nome.compareTo(n.getNome()) > 0) {

			if(n.getDireito() == null) {

				return false;

			} else {

				return buscar(n.getDireito(),nome);
			}
		}


		return false;
	}

	public boolean buscar(String nome) {


		if(raiz == null) {

			return false;

		} else {

			buscar(raiz,nome);

			if(buscar(raiz,nome) == false) {

				return false;

			} else  {

				return true;

			}

		}
	}



	public boolean remover(String nome) {

		if(raiz == null) {

			return false;

		} else {

			if(raiz.getNome().equals(nome)) {

				No aux = new No(" ");
				aux.setEsquerdo(raiz);
				boolean result = raiz.remover(nome,aux);
				raiz = aux.getEsquerdo();
				return result;

			} else {

				return raiz.remover(nome,null);
			}
		}
	}

	public void EmOrdem(No n) {



		if(n.getEsquerdo()!=null) {

			EmOrdem(n.getEsquerdo());
		}
		
		if(!n.getRemove()) {

		System.out.println(n.getNome() + " " +  n.getKill());
		
		}
       

		if(n.getDireito() != null) {

			EmOrdem(n.getDireito());
		}
	}
	

	
	public void EmOrdem() {

		if(raiz != null) {
		
		EmOrdem(raiz);
		}
	}

	public No getRaiz() {
		return raiz;
	}

	public void setRaiz(No raiz) {
		this.raiz = raiz;
	}





}

}
    
 

