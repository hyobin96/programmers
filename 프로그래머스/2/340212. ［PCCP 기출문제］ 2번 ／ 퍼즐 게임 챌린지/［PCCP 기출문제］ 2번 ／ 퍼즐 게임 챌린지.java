import java.util.*;

class Solution {
    boolean isPossible(int level, int[] diffs, int[] times, long limit) {
        long time = 0;
        for (int i = 0; i < diffs.length; i++) {
            time += times[i];
            if (diffs[i] > level) {
                time += (diffs[i] - level) * (times[i - 1] + times[i]);
            }
        }
        return time <= limit;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        int l = 1, r = Arrays.stream(diffs).max().getAsInt();
        int level = 100_000;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (isPossible(mid, diffs, times, limit)) {
                r = mid - 1;
                level = Math.min(level, mid);
            }
            else {
                l = mid + 1;
            }
        }
        
        int answer = level;
        return answer;
    }
}