import java.util.HashSet;

public class Main {
  public static void main(String[] args) {
    HashSet<Integer> set = new HashSet<>();
    StringBuilder sb = new StringBuilder();
    for (Integer i = 1; i < 1000001; i++) {
      if (!set.contains(i)) {
        sb.append(i).append("\n");
      }
      Integer j = i;
      Integer sum = i;
      while (j > 0) {
        sum += j % 10;
        j /= 10;
      }
      set.add(sum);
    }
    System.out.println(sb.delete(sb.length() - 1, sb.length()).toString());
  }
}
