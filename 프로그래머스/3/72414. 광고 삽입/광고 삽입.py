# 윈도우 슬라이딩
def solution(play_time, adv_time, logs):
    def to_minute(t):
        t = list(map(int, t.split(":")))
        return t[0] * 3600 + t[1] * 60 + t[2]
    
    def to_time_format(t):
        h, t = divmod(t, 3600)
        m, s = divmod(t, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    time_map = dict()
    for log in logs:
        t1, t2 = log.split("-")
        t1, t2 = to_minute(t1), to_minute(t2)
        time_map[(t1, 1)] = time_map.get((t1, 1), 0) + 1
        time_map[(t2, -1)] = time_map.get((t2, -1), 0) + 1
        
    # print(time_map)
    time_arr = []
    for k, v in time_map.items():
        time_arr.append((k, v))
        
    time_arr.sort()
    # print(time_arr)
    arr = []
    curr_cnt = 0
    for i, ((t, v), cnt) in enumerate(time_arr):
        if curr_cnt:
            arr.append((s, t, curr_cnt))
        s = t
        curr_cnt += v * cnt
    
    # print(arr)
    
    play_time = to_minute(play_time)
    s, e = 0, to_minute(adv_time)
    seconds_arr = [0] * (play_time + 1)
    for i, (t1, t2, cnt) in enumerate(arr):
        for k in range(t1, t2):
            seconds_arr[k] = cnt
    
    # print(arr)
            
    total_play_time = sum(seconds_arr[:e])
    # print(to_time_format(e))
    # print(to_time_format(total_play_time))
    max_playtime = total_play_time
    adv_start_time = 0
    
    # print(e, play_time)
    while e + 1 <= play_time:
        total_play_time = total_play_time - seconds_arr[s] + seconds_arr[e]
        if max_playtime < total_play_time:
            # print(to_time_format(max_playtime))
            adv_start_time = s + 1
            max_playtime = total_play_time
        s, e = s + 1, e + 1
        
    
    answer = to_time_format(adv_start_time)
    return answer