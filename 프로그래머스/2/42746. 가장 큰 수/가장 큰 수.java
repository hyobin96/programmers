import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> list = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .collect(Collectors.toList());  
        
        list.sort((n1, n2) -> Long.valueOf(n2 + n1).compareTo(Long.valueOf(n1 + n2)));
        
        String answer = String.join("", list);
        
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}