# 규칙, 1 2 3 / 2 2 3 / 3 3 3 
# 1 2 3 4 / 2 2 3 4 / 3 3 3 4 / 4 4 4 4
# i 행 줄에 i + 1이 i + 1 개수만큼, 그 다음은 i + 2, i + 3 ... n
# left // n
def solution(n, left, right):
    arr = []
    
    for i in range(left // n + 1, right // n + 2):
        for _ in range(i):
            arr.append(i)
        for j in range(i + 1, n + 1):
            arr.append(j)
    
    
    return arr[left % n : left % n + right - left + 1]