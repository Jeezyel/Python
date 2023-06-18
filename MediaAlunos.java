import java.util.Scanner;

public class MediaAlunos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] medias = new double[10];
        int contadorAprovados = 0;

        System.out.println("Digite as notas dos 10 alunos:");

        // Lê as notas de cada aluno e calcula a média
        for (int i = 0; i < medias.length; i++) {
            double soma = 0;

            for (int j = 0; j < 4; j++) {
                System.out.print("Digite a nota " + (j + 1) + " do aluno " + (i + 1) + ": ");
                double nota = scanner.nextDouble();
                soma += nota;
            }

            medias[i] = soma / 4;

            if (medias[i] >= 7.0) {
                contadorAprovados++;
            }
        }

        System.out.println("Quantidade de alunos com média maior ou igual a 7.0: " + contadorAprovados);
    }
}
