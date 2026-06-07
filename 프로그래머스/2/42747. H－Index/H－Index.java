import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        int n = citations.length;
        
        int h_index = 0;
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) {
                h_index = n - i;
                break;
            }
        }
        
        int answer = h_index;
        return answer;
    }
}