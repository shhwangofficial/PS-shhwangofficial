import java.io.*;
import java.util.*;

public class input_snippets {
    public static void main(String[] args) throws IOException {
        // 입력 파일 설정 (백준에서는 제거)
        String filePath = "java_input.txt";
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        
        // 표준 입력으로 바꾸고 싶다면: 
        // BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        // N = int(input())
        int N = Integer.parseInt(reader.readLine().trim());

        // a, b = map(int, input().split())
        String[] ab = reader.readLine().trim().split(" ");
        int a = Integer.parseInt(ab[0]);
        int b = Integer.parseInt(ab[1]);

        // list1 = input().split()
        String[] list1 = reader.readLine().trim().split(" ");

        // num = list(map(int, input().split()))
        int[] num = Arrays.stream(reader.readLine().trim().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();

        // num_list = list(map(int, input()))  # 문자열 하나를 받아서 숫자 배열로 변환
        String binaryString = reader.readLine().trim();
        int[] numList = new int[binaryString.length()];
        for (int i = 0; i < binaryString.length(); i++) {
            numList[i] = binaryString.charAt(i) - '0';
        }

        // copied_list = copy.deepcopy(list1)
        String[] copiedList = Arrays.copyOf(list1, list1.length);

        // 입력이 있을 때까지 받기
        List<String> allLines = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            allLines.add(line.trim());
        }

        // 출력 확인 (필요 시 주석 해제)
        // System.out.println("N = " + N);
        // System.out.println("a = " + a + ", b = " + b);
        // System.out.println("list1 = " + Arrays.toString(list1));
        // System.out.println("num = " + Arrays.toString(num));
        // System.out.println("numList = " + Arrays.toString(numList));
        // System.out.println("copiedList = " + Arrays.toString(copiedList));
        // System.out.println("allLines = " + allLines);
    }
}
