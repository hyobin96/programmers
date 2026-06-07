import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        int multiple = Arrays.stream(num_list).reduce(1, (a, b) -> a * b);
        int sum = Arrays.stream(num_list).sum();
        return multiple < sum * sum ? 1 : 0;
    }
}