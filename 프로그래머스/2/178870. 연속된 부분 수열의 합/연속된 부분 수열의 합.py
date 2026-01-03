# 투포인터?
# k보다 크면 앞의 간격 전진, 작으면 뒤에 간격 늘이기
# 길이는 두 인덱스의 차 + 1
# k를 만족한다면 인덱스 저장
# 저장할 때 [길이, 시작, 끝] 로 저장
# 길이가 더 길다면 저장 x
# 길이가 같다면 시작 인덱스가 더 작은 경우 저장
# 길이가 짧다면 그냥 저장

def solution(sequence, k):
    answer = [1_000_001, 0, 0]
    n = len(sequence)
    
    def update(s, e):
        length = e - s + 1
        if length < answer[0]:
            answer[0], answer[1], answer[2] = length, s, e
        elif length == answer[0] and answer[1] > s:
            answer[1], answer[2] = s, e
                
    
    s, e = 0, 0
    total = sequence[0]
    
    while True:
        if total == k:
            update(s, e)
            if e + 1 < n:
                total -= sequence[s]
                s += 1
                e += 1
                total += sequence[e]
            else:
                break
        elif total < k:
            e += 1
            if e == n:
                break
            total += sequence[e]
        else:
            total -= sequence[s]
            s += 1
            if s == n:
                break
    
    return [answer[1], answer[2]]