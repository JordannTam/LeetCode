import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'findMinCost' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY efficiency as parameter.
     */

    public static int findMinCost(List<Integer> efficiency) {
    // Write your code here
        List<Integer> sorted = new ArrayList<>(efficiency);

        Collection.sorted(sorted);




        return 0;
        
        
        

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int efficiencyCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> efficiency = IntStream.range(0, efficiencyCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.findMinCost(efficiency);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
