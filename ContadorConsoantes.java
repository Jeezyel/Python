/*import java.util.ArrayList;
import java.util.Scanner;

public class teste{
    static int valor[] = new int[5];;
    public static void main(String[] args) {
    Scanner leitor = new Scanner(System.in);

    String consoantes[] = {"B" ,"C" ,"D" ,"F" ,"G" ,"H" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" , "Q" ,"R" ,"S" ,"T" ,"V" ,"W" ,"X" ,"Y" ,"Z" };
    String letras[] = new String[10];
    Integer quantidadeConsoantes = 0;

    for (int j = 0; j < 10 ; j++) {

        System.out.println("informe uma letra");
        letras[j] = leitor.next();
    
    }

    ArrayList<String> consoantesSemelhantes = new ArrayList<String>();
    
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < consoantes.length; j++) {
            if (letras[i].toUpperCase() == consoantes[j]) {
                consoantesSemelhantes.add(letras[i]);

                quantidadeConsoantes++;
            }else{
                System.out.println(" esta no else" + quantidadeConsoantes);
                quantidadeConsoantes++;
            }
        }
    }

    System.out.println("consoantes foram lidas: " + consoantesSemelhantes );
    System.out.println("quantidade lidas: " + quantidadeConsoantes );

}


}

 */

import java.util.Scanner;

public class ContadorConsoantes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[] vetor = new char[10];
        
        System.out.println("Digite 10 caracteres:");

        // Lê os caracteres e armazena no vetor
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = scanner.next().charAt(0);
        }

        int contadorConsoantes = 0;
        StringBuilder consoantes = new StringBuilder();

        // Verifica se cada caractere é uma consoante e conta e armazena as consoantes
        for (char c : vetor) {
            if (Character.isLetter(c) && !isVowel(c)) {
                contadorConsoantes++;
                consoantes.append(c).append(" ");
            }
        }

        System.out.println("Quantidade de consoantes: " + contadorConsoantes);
        System.out.println("Consoantes encontradas: " + consoantes.toString().trim());
    }

    // Verifica se um caractere é uma vogal
    private static boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}




