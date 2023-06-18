import java.util.ArrayList;
import java.util.Scanner;

public class teste{
    static int valor[] = new int[5];
    static ArrayList<Integer> listNumeros = new ArrayList<>();
    static ArrayList<Integer> inpar = new ArrayList<>();
    static ArrayList<Integer> par = new ArrayList<>();
    public static void main(String[] args) {
    Scanner leitor = new Scanner(System.in);

    String consoantes[] = {"B" ,"C" ,"D" ,"F" ,"G" ,"H" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" , "Q" ,"R" ,"S" ,"T" ,"V" ,"W" ,"X" ,"Y" ,"Z" };
    String letras[] = new String[10];
    Integer quantidadeConsoantes = 0;


    

    for (int j = 0; j < 20 ; j++) {

        System.out.println("informe um numero");
        
        listNumeros.add(leitor.nextInt());
    
    }

    
    
    for (int i = 0; i < listNumeros.size(); i++) {
        if ((listNumeros.get(i) % 2) == 0) {
            par.add(listNumeros.get(i));
        }else{
            inpar.add(listNumeros.get(i));
        }
    }

    

    System.out.println("impar: " + inpar );
    System.out.println("par: " + par );

}


}

