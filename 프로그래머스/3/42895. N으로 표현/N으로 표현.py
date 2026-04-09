def solution(N, number):
    dp = [set() for _ in range(9)]
    n_str = str(N)
    for i in range(1, 9):
        dp[i].add(int(n_str))
        n_str += str(N)
    
    for i in range(2, 9):
        for j in range(1, i):
            k, l = i - j, j
            for n1 in dp[k]:
                for n2 in dp[l]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)
                    
    min_count = -1
    for i in range(1, 9):
        if number in dp[i]:
            min_count = i
            break
    answer = min_count
    return answer