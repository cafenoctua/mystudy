import java.util.Scanner;

/**
 * Survey
 */
public class Survey {

    public static void main(String[] args) {
        System.out.println("Wellcome. Thank you for taking the survey.");

        Scanner scanner = new Scanner(System.in);
        Integer counter = 0;

        System.out.println("What is your name?");
        String name = scanner.nextLine();
        counter++;

        System.out.println("How much money do you spend on coffee?");
        double coffeePrice = scanner.nextDouble();
        counter++;


        System.out.println("How much money do you spend on fast food?");
        double foodPrice = scanner.nextDouble();
        counter++;

        System.out.println("How many times a week do you buy coffee?");
        Integer coffeeAmount = scanner.nextInt();
        counter++;

        System.out.println("How many times a week do you buy fast food?");
        Integer foodAmount = scanner.nextInt();
        counter++;

        // Output input params
        System.out.println("Thank you " + name + " for answering all " + counter + " questions.");
        System.out.println("Weekly, you spend $ " + (coffeeAmount * coffeePrice) + " on coffee.");
        System.out.println("Weekly, you spend $ " + (foodAmount * foodPrice) + " on food.");
    }
}