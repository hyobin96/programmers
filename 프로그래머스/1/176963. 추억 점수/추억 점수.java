import java.util.*;

class Solution {
    
    static Map<String, Integer> map = new HashMap<>();
    
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        for (int i = 0; i < name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        
        int[] scores = new int[photo.length];
        
        for (int i = 0; i < photo.length; i++) {
            int score = 0;
            for (String n : photo[i]) {
                score += map.getOrDefault(n, 0);
            }
            
            scores[i] = score;
        }
        
        int[] answer = scores;
        return answer;
    }
}