# 맨 앞에서 뒤로 가면서 뒤보다 작으면 삭제
# 효율적인 자료구조? 이중연결리스트가 제일 좋아보임
# 근데 만들기 너무 귀찮은데
# stack이 제일 낫네

def solution(number, k):
    stack = []
    for num in number:
        num = int(num)
        while stack and stack[-1] < num and k:
            stack.pop()
            k -= 1
        stack.append(num)
    
    while k:
        stack.pop()
        k -= 1
        
    stack = list(map(str, stack))
    return ''.join(stack)