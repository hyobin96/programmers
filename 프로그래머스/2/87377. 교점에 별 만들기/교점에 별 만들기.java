// 교점 Star class
// A, B, E  C, D, F 를 받아 교점을 구하는 메서드
// 연산은 모두 long으로 연산
// 정답 크기가 1000 * 1000 이므로 minx, miny, maxx, maxy를 구해야 함
// 배열 크기는 [maxy-miny][maxx-minx]
// x는 minX만큼 당겨짐, y는 minY만큼 당겨짐
// 배열에 넣으면 거꾸로 그려지므로 마지막 인덱스부터 넣기

import java.util.*;

class Solution {
    static class Star{
        long x, y;
        
        public Star(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
    
    Star getStar(int[] line1, int[] line2){
        long A = line1[0];
        long B = line1[1];
        long E = line1[2];
        long C = line2[0];
        long D = line2[1];
        long F = line2[2];
        
        long 분모 = A * D - B * C;
        if (분모 == 0) {
            return null;
        }
        long x분자 = B * F - E * D;
        long y분자 = E * C - A * F;
        if (x분자 % 분모 != 0 || y분자 % 분모 != 0){
            return null;
        }
        return new Star(x분자 / 분모, y분자 / 분모);
    }
    
    static long minX = Long.MAX_VALUE;
    static long maxX = Long.MIN_VALUE;
    static long minY = Long.MAX_VALUE;
    static long maxY = Long.MIN_VALUE;
    
    void update(Star star){
        minX = Math.min(minX, star.x);
        maxX = Math.max(maxX, star.x);
        minY = Math.min(minY, star.y);
        maxY = Math.max(maxY, star.y);
    }
    
    public String[] solution(int[][] line) {
        Set<Star> stars = new HashSet<>();
        int n = line.length;
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n; j++) {
                Star star = getStar(line[i], line[j]);
                if (star == null) continue;
                update(star);
                stars.add(star);
            }
        }
        
        char[][] grid = new char[(int)(maxY - minY + 1)][(int)(maxX - minX + 1)];
        for (char[] gr : grid){
            Arrays.fill(gr, '.');
        }
        for (Star star : stars) {
            long x = star.x - minX;
            long y = star.y - minY;
            grid[(int)y][(int)x] = '*';
        }
        
        int len = grid.length;
        
        String[] answer = new String[len];
        for (int i = len - 1; i >= 0; i--) {
            answer[i] = new String(grid[len - 1 - i]);
        }
        
        return answer;
    }
}