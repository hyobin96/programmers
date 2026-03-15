import heapq

def solution(n, t, m, timetable):
    def to_minute(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m
    def to_h_m(t):
        h, m = str(t // 60), str(t % 60)
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        return h + ":" + m
    
    pq = []
    for ti in timetable:
        ti = to_minute(ti)
        heapq.heappush(pq, ti)
        
        
    last_arr_t = -1
    shu_arr_t = 540
    while n > 0:
        crew_arr_t = 0
        cnt = 0
        while pq and pq[0] <= shu_arr_t and cnt < m:
            crew_arr_t = heapq.heappop(pq)
            cnt += 1
        if cnt == m:
            last_arr_t = crew_arr_t - 1
        elif cnt < m:
            last_arr_t = shu_arr_t  

        shu_arr_t += t
        n -= 1
    
    answer = to_h_m(last_arr_t)
    return answer