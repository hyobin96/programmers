import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted((n1, n2) -> (n2 + n1).compareTo(n1 + n2))
            .collect(joining());  
                
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}