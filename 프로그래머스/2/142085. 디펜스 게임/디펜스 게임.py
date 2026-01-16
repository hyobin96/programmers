# 적의 수가 많은 순서대로 무적권을 쓰는 게 직관적으로 좋아보임
# enemy 수를 순서대로 더하면서 n을 초과하면 그 중 병사의 수가 가장 많은 것 - 해주고 무적권-  하고 넘어가기
# 그럼 매번 가장 많은 병사의 수를 알아야 함
# 이건 pq

import heapq

def solution(n, k, enemy):
    pq = []
    
    answer = 0
    for i, e in enumerate(enemy):
        heapq.heappush(pq, -e)
        n -= e
        if n < 0:
            if k == 0:
                return i
            n -= heapq.heappop(pq)
            k -= 1
    
    return len(enemy)