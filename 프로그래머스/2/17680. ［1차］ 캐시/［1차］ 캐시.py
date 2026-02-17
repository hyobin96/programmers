# 가장 오랫동안 사용되지 않은 도시이름 교체
# key: 도시이름, value: 사용한 시점, idx
# cache크기는 최대 30

def solution(cacheSize, cities):
    # 소문자로 통일
    cities = [city.lower() for city in cities]
    
    cache = dict()
    cache_idx = []
    
    ex_time = 0
    for idx, city in enumerate(cities):
        if city in cache:
            cache[city] = idx
            ex_time += 1
        else:
            cache[city] = idx
            if len(cache) > cacheSize:
                lru = sorted(list(cache.items()), key=lambda item: item[1])[0]
                # print(lru)
                del cache[lru[0]]
                    
            ex_time += 5
            
    answer = ex_time
    return answer