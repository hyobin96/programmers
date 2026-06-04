class Solution {
    public int solution(int n, int m, int[] section) {
        int i = 0, j = 0, count = 1;
        while (i < section.length && j < section.length) {
            if (section[j] - section[i] + 1 <= m) {
                j += 1;
            }
            else {
                i = j;
                count++;
            }
        }
        
        int answer = count;
        return answer;
    }
}