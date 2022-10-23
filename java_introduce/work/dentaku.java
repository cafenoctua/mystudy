class Dentaku{
  public static void main(String[] args){
    Dentaku dentaku = new Dentaku();
    dentaku.plus(10, 5);
    dentaku.minus(9, 2);
  }

  void plus(int val1, int val2){
    System.out.println(val1 + val2);
  }

  void minus(int val1, int val2){
    System.out.println(val1 - val2);
  }
}