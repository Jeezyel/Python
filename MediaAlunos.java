import java.util.ArrayList;
import java.util.Scanner;

/*
Faça um Programa que crie um vetor de 5 números inteiros. Em seguida, mostre a 
soma, a multiplicação e os números 
*/

public class MediaAlunos {

    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
       ArrayList<Double> notas = new ArrayList<Double>();

       Boolean finalizar = true;
        while(finalizar){
            System.out.println("infome um numero: ");
            notas.add(leia.nextDouble());

            System.out.println("deseja informa outro numero 1= Sim 2=Não" );
            if (leia.nextInt()== 2 ) {
                finalizar = false;
            }
        }

        System.out.println(" quantidade de que foram lidas "  );



        leia.close();
    }
}
