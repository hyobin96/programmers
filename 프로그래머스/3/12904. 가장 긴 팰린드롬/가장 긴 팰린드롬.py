def solution(s):
    def count_palindrome(left, right, count):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
            count += 2
        return count
        
    max_length = 1
    for i in range(len(s) - 1):
        max_length = max(max_length, count_palindrome(i - 1, i + 1, 1))
        if s[i] == s[i + 1]:
            max_length = max(max_length, count_palindrome(i - 1, i + 2, 2))
        
    answer = max_length

    return answer