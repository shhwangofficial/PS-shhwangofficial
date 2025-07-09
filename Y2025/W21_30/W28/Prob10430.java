import java.io.*;
import java.util.Arrays;

public class Prob10430 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int[] num = Arrays.stream(reader.readLine().trim().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();
        int A = num[0];
        int B = num[1];
        int C = num[2];
        System.out.println((A+B)%C);
        System.out.println((((A%C)+(B%C))%C));
        System.out.println((A*B)%C);
        System.out.println((((A%C)*(B%C))%C));
    }
}
