import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ExampleOne {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("greetings.txt");
        } catch (FileNotFoundException e) {
            // TODO: handle exception
            System.out.println(e.getMessage());
        }
    }
    
}