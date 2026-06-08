class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int t = 0, curr_health = health;
        for (int[] attack : attacks) {
            int a_t = attack[0], damage = attack[1];
            
            int gap_t = attack[0] - t - 1;
            curr_health += gap_t * bandage[1] + (gap_t / bandage[0]) * bandage[2];
            if (curr_health > health) curr_health = health;
            
            curr_health -= damage;
            t = attack[0];
            // System.out.println(curr_health + " " + t + " " + gap_t);
            if (curr_health <= 0) return -1;
        }
        
        int answer = curr_health;
        return answer;
    }
}