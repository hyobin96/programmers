# 스택 개념

def solution(numbers):
    n = len(numbers)
    
    stack = []
    answer = [-1] * n
    max_num = 0
    for i in range(n - 1, -1, -1):
        number = numbers[i]
        while stack and stack[-1] <= number:
            stack.pop()
        if stack:
            answer[i] = stack[-1]    
        stack.append(number)
                    
    return answer