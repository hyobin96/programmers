import java.util.*;

class Solution {
    static Map<Character, Integer > map = new HashMap<>();
    
    public int[] solution(String[] keymap, String[] targets) {
        for (String s : keymap) {
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                map.put(c, Math.min(map.getOrDefault(c, 100), i + 1));
            }
        }
        
        // System.out.println(map);
        
        int[] counts = new int[targets.length];
        for (int i = 0; i < targets.length; i++) {
            for (char c : targets[i].toCharArray()) {
                int count = map.getOrDefault(c, 0);
                if (count == 0) {
                    counts[i] = -1;
                    break;
                }
                counts[i] += count;
            }
        }
        
        
        int[] answer = counts;
        return answer;
    }
}