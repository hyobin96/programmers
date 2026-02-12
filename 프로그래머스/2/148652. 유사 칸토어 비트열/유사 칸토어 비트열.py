# 1 -> 11011, 0 > 00000
# + 2()
# * 5씩 개수가 늘어남
# 5 ** 20? = 너무큼
# q 이용?
# 5씩 구간을 나눠서 판정이 필요
# 1
# 11011  4
# 11011 11011 00000 11011 11011
#   4     4     0     4     4
#   16    16    0     16    16


def solution(n, l, r):
    def counting(end, s, u):
        total = 0
        while end != 0:
            몫 = end // s
            total += 몫 * u if 몫 < 3 else (몫 - 1) * u
            if 몫 == 2:
                break
            end %= s
            s //= 5
            u //= 4
        
        return total
    
    scale = 5 ** (n - 1)
    unit = 4 ** (n - 1)
    
    total = counting(r, scale, unit) - counting(l - 1, scale, unit)
    
    answer = total
    return answer