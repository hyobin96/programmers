class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        int j = 0, k = 0;
        for (int i = 0; i < goal.length; i++) {
            if (j < cards1.length && goal[i].equals(cards1[j])) {
                j++;
                continue;
            }
            if (k < cards2.length && goal[i].equals(cards2[k])) {
                k++;
                continue;
            }
            
            answer = "No";
        }

        return answer;
    }
}