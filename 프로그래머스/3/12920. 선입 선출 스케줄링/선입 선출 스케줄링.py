import math

def solution(n, cores):
    def mapping(cores, seconds_core_map):
        for i, second in enumerate(cores, start = 1):
            seconds_core_map[second] = seconds_core_map.get(second, [])
            seconds_core_map[second].append(i)
        return seconds_core_map
    
    def is_possible(mid, n, seconds_core_map):
        for second, core in seconds_core_map.items():
            q, r = divmod(mid, second)
            n -= (q + 1) * len(core)
        return n <= 0
    
    if n <= len(cores):
        return n
    
    seconds_core_map = mapping(cores, dict())
    
    left, right = 1, 50000
    print(right)
    min_seconds = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid, n, seconds_core_map):
            right = mid - 1
            min_seconds = min(min_seconds, mid)
        else:
            left = mid + 1
    
    # print(min_seconds)
    prev_seconds = min_seconds - 1
    for second, core in seconds_core_map.items():
        q, r = divmod(prev_seconds, second)
        n -= (q + 1) * len(core)
    
    # print(cores)
    # print(n, min_seconds)
    last_core = 0
    for i, second in enumerate(cores, start = 1):
        if min_seconds % second == 0:
            n -= 1
            if n == 0:
                last_core = i
                break
    
    return last_core