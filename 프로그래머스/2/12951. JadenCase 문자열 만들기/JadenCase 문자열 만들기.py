def solution(s):
    JadenCase = [s[0].upper()]
    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            JadenCase.append(s[i].upper())
        else:
            JadenCase.append(s[i].lower())
    answer = ''.join(JadenCase)
    return answer