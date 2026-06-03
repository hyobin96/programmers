import java.util.*;

class Solution {
    
    static Map<String, Integer> nameToRank = new HashMap<>();
    
    void swap(String[] players, String name) {
        int rank = nameToRank.get(name);
        String prevName = players[rank - 1];
        players[rank - 1] = players[rank];
        players[rank] = prevName;
        
        nameToRank.put(name, rank - 1);
        nameToRank.put(prevName, rank);
        
    }
    
    public String[] solution(String[] players, String[] callings) {
        for (int i = 0; i < players.length; i++) {
            nameToRank.put(players[i], i);   
        }
        
        for (String callName : callings) {
            swap(players, callName);
        }
    
        String[] answer = players;
        return answer;
    }
}