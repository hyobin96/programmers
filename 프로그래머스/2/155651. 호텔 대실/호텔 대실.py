# 입실 시간 기준으로 정렬
# 퇴실 시간 기준으로 pq
# pq에서 입실할 손님의 입장시간 - 10분보다 pq[0]의 퇴실시간이 이하면 다 퇴실
# 그 다음 pq에 삽입
# pq의 최대 크기가 result

import heapq

def solution(book_time):
    def get_minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    for b_t in book_time:
        b_t[0] = get_minute(b_t[0])
        b_t[1] = get_minute(b_t[1])

    
    book_time.sort()
    pq = []
    answer = 0
    
    for b in book_time:
        while pq and pq[0][0] <= b[0] - 10:
            heapq.heappop(pq)
        heapq.heappush(pq, (b[1], b[0]))
        # print(pq)
        answer = max(answer, len(pq))
        
    return answer