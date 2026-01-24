# 1이 최초로 있는 자리 + 1 자리에서 최소 수가 존재
# 1111 -> 10111
# 1개 바꾸기, 2개 바꾸기
# 전부 1인 경우 첫 자리 0 하고 다음 자리수 1
# 101010 -> 101011
# 10111001 -> 최초 0인걸 찾고 그 뒤에 1 더하기


def solution(numbers):
    answer = []
    for number in numbers:
        num = number
        exp = -1
        while num % 2 != 0:
            num //= 2
            exp += 1      
        exp = exp if exp > 0 else 0
        answer.append(number + 2 ** exp)
    
    return answer