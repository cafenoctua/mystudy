import java.util.List;

/**
 * Main
 */
public class Main {
  public void processData(List<String[]> data) {
      for (String[] record : data) {
          // データの処理を行う (ここでは標準出力に表示)
          for (String value : record) {
              System.out.print(value + " ");
          }
          System.out.println();  // 改行
      }
  }
  public static void main(String[] args) {
    String csvFilePath = "resources/sample.csv";
    String csvDelimiter = ",";
    CSVReader csvReader = new CSVReader(csvFilePath, csvDelimiter);
    List<String[]> data = csvReader.readCSV();
    

    CSVConverter csvConverter = new CSVConverter(2);
    List<String[]> convertedData = csvConverter.convertData(data);
    Main a = new Main();
    a.processData(convertedData);
  }
}