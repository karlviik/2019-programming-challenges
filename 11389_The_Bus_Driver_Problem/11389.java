import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // put answer to a stringbuilder for speed
        StringBuilder answer = new StringBuilder();
        while (true) {
            // get all the thingy things in
            int drivers = scan.nextInt();
            int totalHours = scan.nextInt();
            int r = scan.nextInt();
            // if it's the end of input, break out and print answers
            if (drivers == 0 && totalHours == 0 && r == 0) {
                break;
            }
            // put all morning routes in array and sort them
            int[] morning = new int[drivers];
            for (int i = 0; i < drivers; i++) {
                morning[i] = scan.nextInt();
            }
            Arrays.sort(morning);
            // put all evening routes in array and sort them
            int[] evening = new int[drivers];
            for (int i = 0; i < drivers; i++) {
                evening[i] = scan.nextInt();
            }
            Arrays.sort(evening);
            // each driver gets the n'th morning route and allRoutes - n 'th evening route
            int sum = 0;
            for (int i = 0; i < drivers; i++) {
                int temp = (morning[i] + evening[drivers - i - 1]);
                sum += (temp > totalHours) ? temp - totalHours : 0;
            }
            // calculate the overtime pay and add to answer
            answer.append((sum * r));
        }
        System.out.println(String.join("\n", answer));
    }
}