import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> list = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted((n1, n2) -> (n2 + n1).compareTo(n1 + n2))
            .collect(Collectors.toList());  
                
        String answer = String.join("", list);
        
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}