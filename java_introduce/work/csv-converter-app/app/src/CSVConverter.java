import java.util.ArrayList;
import java.util.List;

public class CSVConverter {
  private int columnToConvert;

  public CSVConverter(int columnToConvert) {
      this.columnToConvert = columnToConvert;
  }
  public List<String[]> convertData(List<String[]> data) {
    List<String[]> convertedData = new ArrayList<>();
    for (String[] record : data) {
      if (record.length > columnToConvert) {
        record[columnToConvert] = record[columnToConvert].toUpperCase();
      }
      convertedData.add(record);
    }
    return convertedData;
  }
}