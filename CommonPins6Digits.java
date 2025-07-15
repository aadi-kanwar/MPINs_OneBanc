public class CommonPins6Digits {
  public static void main(String[] args) {
    System.out.println("Common 4 Digit Pins");
    for(int i = 0; i <= 9;i++) {
      System.out.print("\""+i+i+i+i+i+i+"\", ");
    }

    for(int i = 0; i <= 4;i++) {
      int j = i + 1, k= i + 2, l= i + 3, m= i + 4, n= i + 5;
      System.out.print("\""+i + j + k +l +m + n +"\", ");
    }

    for(int i = 9; i > 4; i--) {
      int j = i - 1, k= i - 2, l = i - 3, m = i - 4, n = i - 5;
      System.out.print("\""+i + j + k +l +m +n +"\", ");
    }

    for (int i = 0; i <= 9; i++) {
      int j = i + 1;
      if (i == 9)
        j = 0;
      System.out.print("\"" + i + i + i + j + j + j + "\", ");
      System.out.print("\"" + j + j + j + i + i + i + "\", ");
    }
    
    for (int i = 0; i <= 7; i++) {
      int j = i + 1, k = i + 2 ;
      System.out.print("\"" + i + i + j + j + k + k + "\", ");
      System.out.print("\"" + k + k + j + j + i + i + "\", ");
    }
  }
}