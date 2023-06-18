import java.util.ArrayList;
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

    ArrayList<String> consoantesSemelhantes = null;
    
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < consoantes.length; j++) {
            if (letras[i].toUpperCase() != consoantes[j]) {
                consoantesSemelhantes.add(letras[i]);

                quantidadeConsoantes++;
            }
        }
    }

    System.out.println("consoantes foram lidas: " + consoantesSemelhantes );
    System.out.println("quantidade lidas: " + quantidadeConsoantes );

}


}