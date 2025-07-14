// import java.util.*;
public class CommonPins {
  public static void main(String[] args) {
    // Scanner sc = new Scanner(System.in);
    System.out.println("Common 4 Digit Pins");
    for(int i = 0; i <= 9;i++) {
      System.out.print("\""+i+i+i+i+"\", ");
    }
    for(int i = 0; i <= 6;i++) {
      int j = i + 1, k= i + 2, l= i + 3;
      System.out.print("\""+i + j + k +l +"\", ");
    }
    for(int i = 9; i >= 3; i--) {
      int j = i - 1, k= i - 2, l = i - 3;
      System.out.print("\""+i + j + k +l +"\", ");
    }
    for (int i = 0; i <= 9; i++) {
      int j = i + 1;
      if (i == 9)
        j = 0;
      System.out.print("\"" + i + i + j + j + "\", ");
    }
  }
}