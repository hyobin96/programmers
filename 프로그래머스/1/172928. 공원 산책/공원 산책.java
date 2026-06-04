import java.util.*;

class Solution {
    
    static Map<String, Integer> map = new HashMap<>();
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    
    public int[] solution(String[] park, String[] routes) {
        map.put("N", 0);
        map.put("S", 1);
        map.put("W", 2);
        map.put("E", 3);
        
        int n = park.length;
        int m = park[0].length();
        
        int r = 0;
        int c = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (park[i].charAt(j) == 'S') {
                    r = i;
                    c = j;
                    break;
                }
            }
        }
        
        for (String route : routes) {
            // System.out.println(r + " " + c);
            
            String[] temp = route.split(" ");
            int d = map.get(temp[0]);
            int cnt = Integer.valueOf(temp[1]);
            
            int nr = r;
            int nc = c;
            
            boolean isPossible = true;
            for (int i = 0; i < cnt; i++) {
                nr += dr[d];
                nc += dc[d];
                
                if (nr >= n || nr < 0 || nc >= m || nc < 0
                   || park[nr].charAt(nc) == 'X') {
                    isPossible = false;
                    break;
                }
            }
            
            if (!isPossible) {
                continue;
            }
            
            r = nr;
            c = nc;
        }
        
        
        int[] answer = {r, c};
        return answer;
    }
}