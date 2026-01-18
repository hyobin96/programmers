# 각 번호를 선택했을 때 한 그룹이 만들어짐.
# 이 그룹에서 어떤 번호로 시작해도 같은 그룹이 만들어짐.
# 상자의 번호와 들어있는 카드의 숫자가 일치하는 상자는 골라도 개수가 1이라 마지막에 고른다고 생각.
# 그럼 최고 점수는 각 그룹들에 속한 상자의 수들을 곱한 것

def solution(cards):
    cards = [0] + cards
    
    l = []
    s = set()
    for i in range(1, len(cards)):
        if i == cards[i]:
            l.append(1)
            continue
        if i in s:
            continue
        cnt = 0
        while i not in s:
            s.add(i)
            i = cards[i]
            cnt += 1

        l.append(cnt)
    
    l.sort(reverse=True)
    
    answer = 0
    if len(l) > 1:
        answer = l[0] * l[1]
    
    return answer