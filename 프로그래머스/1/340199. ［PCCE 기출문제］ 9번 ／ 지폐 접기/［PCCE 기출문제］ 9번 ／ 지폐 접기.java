class Solution {
    
    boolean isPossible(int[] wallet, int[] bill){
        if (wallet[0] >= bill[0] && wallet[1] >= bill[1]) {
            return true;
        }
        if (wallet[0] >= bill[1] && wallet[1] >= bill[0]) {
            return true;
        }
        return false;
    }
    
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        while (true) {
            if (bill[0] < bill[1]) {
                int tmp = bill[0];
                bill[0] = bill[1];
                bill[1] = tmp;
            }
            
            if (isPossible(wallet, bill)) {
                break;
            }
            
            if (bill[0] > bill[1]) {
                bill[0] /= 2;
            }
            else {
                bill[1] /= 2;
            }
            
            answer++;
        }
        
        return answer;
    }
}