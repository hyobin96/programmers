import java.util.*;

class Solution {
    static Map<String, Integer> map = new HashMap<>();
    
    public int solution(String[] friends, String[] gifts) {
        int k = 0;
        for (String name : friends) {
            map.put(name, k++);
        }
        
        int n = friends.length;
        int[][] giftRecord = new int[n][n];
        
        for (String str : gifts) {
            String[] names = str.split(" ");
            int u = map.get(names[0]);
            int v = map.get(names[1]);
            
            giftRecord[u][v] += 1;
        }
        
        int[] giftScore = new int[n];
        for (int i = 0; i < n; i++) {
            int score = 0;
            for (int j = 0; j < n; j++) {
                score += giftRecord[i][j] - giftRecord[j][i];
            }
            // System.out.println(score);
            giftScore[i] = score;
        }
        
        // System.out.println(Arrays.toString(giftScore));
        
        int[] nextMonthGiftNums = new int[n];
        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (giftRecord[i][j] == giftRecord[j][i]) {
                    if (giftScore[i] > giftScore[j]) {
                        nextMonthGiftNums[i] += 1;
                    }
                }
                else {
                    if (giftRecord[i][j] > giftRecord[j][i]) {
                        nextMonthGiftNums[i] += 1;
                    }
                }
            }
        }
        
        // System.out.println(Arrays.toString(nextMonthGiftNums));
        int maxGiftNum = 0;
        for (int num : nextMonthGiftNums) {
            maxGiftNum = maxGiftNum < num ? num : maxGiftNum;
        }
        
        int answer = maxGiftNum;
        return answer;
    }
}