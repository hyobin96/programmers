# 눌러야 하는 위치에 인접한 가장 가까운 손가락이 누르는 게 최선?
# 하지만 12121212 라면? 한 손가락만 움직일 수도 있음
# 순서가 중요, 문제는 매번 제일 가까운 걸 움직이는 것이 최선을 보장하지 않음
# 매번 분기? 그럼 2 ** 100_000
# 그럼 dp? 현재 손가락의 위치가 같고 가중치가 같다면 이전까지 어떻게 왔는지는 상관없음
# 3차원 dp?

def solution(numbers):
    keypad = {1: (0, 0), 2:(0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7:(2, 0), 8: (2, 1), 9 :(2, 2), 0: (3, 1)}
    def calculate_weight(curr_num, next_num):
        x1, y1 = keypad[curr_num]
        x2, y2 = keypad[next_num]
        weights = 0
        
        while x1 != x2 or y1 != y2:
            # print(x1, y1, x2, y2)
            if x1 == x2 and y1 != y2:
                weights += abs(y1 - y2) * 2
                y1 = y2
            elif x1 != x2 and y1 == y2:
                weights += abs(x1 - x2) * 2
                x1 = x2
            else:
                if x1 < x2:
                    x1 += 1
                if y1 < y2:
                    y1 += 1
                if x1 > x2:
                    x1 -= 1
                if y1 > y2:
                    y1 -= 1
                weights += 3
        return weights
    
    
    n = len(numbers)
    MAX = 2e9
    dp = [[[MAX] * 10 for _ in range(10)] for _ in range(n + 1)]
    dp[0][4][6] = 0
    
    # print(calculate_weight(1, 0))   
    
    for k in range(n):
        for i in range(10):
            for j in range(10):
                if dp[k][i][j] == MAX:
                    continue
                num = int(numbers[k])
                if num == i or num == j:
                    dp[k + 1][i][j] = min(dp[k][i][j] + 1, dp[k + 1][i][j])
                    continue
                dp[k + 1][i][num] = min(dp[k][i][j] + calculate_weight(j, num), dp[k + 1][i][num])
                dp[k + 1][num][j] = min(dp[k][i][j] + calculate_weight(i, num), dp[k + 1][num][j])
    
    min_weight = 2e9
    for i in range(10):
        for j in range(10):
            # print(dp[n][i][j])
            min_weight = min(dp[n][i][j], min_weight)
    
    answer = min_weight
    return answer