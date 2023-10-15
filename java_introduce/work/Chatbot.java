import java.util.Scanner;

/**
 * Chatbot
 */
public class Chatbot {

    public static void main(String[] args) {
        
        // Define scanner
        Scanner scanner = new Scanner(System.in);
        
        // input name
        System.out.println("Hello. What is your name?");
        String name = scanner.nextLine();
        
        // chatbot's greeting
        System.out.println("Hi " + name + " I'm Javabot. Where are you from?");
        String whereFrom = scanner.nextLine();
        System.out.println("I hear it's so beatiful " + whereFrom + ". I'm from Oracle.");
        
        // ask user age
        System.out.println("How old are you?");
        Integer age = scanner.nextInt();
        System.out.println("So you're " + age +". I'm 400 old.");

        // ask favorite language
        System.out.println("What your favorite language?");
        String language = scanner.nextLine();
        System.out.println(language + " that's greate!");
    }
}`