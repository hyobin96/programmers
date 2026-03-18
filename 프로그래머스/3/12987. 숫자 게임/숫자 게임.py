# 7 5 3 2
# 8 6 3 2
def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    i, j = 0, 0
    score = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            score += 1
            i += 1
            j += 1
        else:
            i += 1
            
    answer = score
    return answer