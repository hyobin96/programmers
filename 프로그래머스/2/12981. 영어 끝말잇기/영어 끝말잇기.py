def solution(n, words):
    prev_words = set()

    result = [0, 0]
    prev = ''
    for i, word in enumerate(words):
        idx = i % n
        if word in prev_words or (prev and prev[-1] != word[0]) or len(word) == 1:
            result = [idx + 1, i // n + 1]
            break
        prev_words.add(word)
        prev = word
        
    answer = result
    return answer