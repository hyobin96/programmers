import java.util.*;

class Solution {
    static Set<Character> set = new HashSet<>();
    
    char encode(char c, int count) {
        while (count > 0) {
            c++;
            if (c > 'z') c = 'a';
            if (!set.contains(c)) count--;
        }
        return (char) c;
    }
    
    public String solution(String s, String skip, int index) {
        for (char c : skip.toCharArray()) {
            set.add(c);
        }
        
        StringBuilder builder = new StringBuilder();
        for (char c : s.toCharArray()) {
            builder.append(encode(c, index));
        }
        
        String answer = builder.toString();
        return answer;
    }
}