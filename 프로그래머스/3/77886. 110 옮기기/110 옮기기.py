# 스택에 넣으면서 110을 찾는다 ...
# 찾았을 때 앞에 옮겨야 할 데가 있다면?
# 옮겨야 할 곳은 어떻게 알지 ..
# 비어있다면? 일단 들고있는다
# 계속 넣다가 들어가야 할 곳을  찾으면? 넣기
# 없다면? 마지막에 붙이기
# 들어가야 할 곳은 어디인가 ... 가장 가까운 0 뒤

def solution(s):
    result = []
    for x in s:
        x = list(x)
        stack = []
        cnt = 0
        for e in x:
            stack.append(e)
            if stack[-3 : ] == ["1", "1", "0"]:
                for _ in range(3):
                    stack.pop()
                cnt += 1
            
        zero_pos = -1
        for i, e in enumerate(stack):
            if e == '0':
                zero_pos = i
        result.append(''.join(stack[ : zero_pos + 1]) + "110" * cnt + ''.join(stack[zero_pos + 1 : ]))
        
        
    answer = result
    return answer