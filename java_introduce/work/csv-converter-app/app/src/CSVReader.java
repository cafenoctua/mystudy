import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * CSVReader
 */
public class CSVReader {

  private String csvFile;
  private String csvDelimiter;

  public CSVReader(String csvFile, String csvDelimiter) {
    this.csvFile = csvFile;
    this.csvDelimiter = csvDelimiter;
  }

  public List<String[]> readCSV() {
    List<String[]> records = new ArrayList<>();

    try(BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
      String line;
      while ((line = br.readLine()) != null) {
        String[] values = line.split(csvDelimiter);
        records.add(values);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    return records;
  } 
}