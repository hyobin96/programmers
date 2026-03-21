def solution(message, spoiler_ranges):
    split_message = message.split(" ")
    words = []  # (s, e, word)
    s, e = 0, 0 
    for word in split_message:
        e = s + len(word) - 1
        words.append((s, e, word))
        s = e + 2
    
    # print(words)
    prevent_spo_words = set()
    for i, (s2, e2, word) in enumerate(words):
        for s1, e1 in spoiler_ranges:
            if not (s2 > e1 or e2 < s1):
                prevent_spo_words.add(i)
            # if s1 > e2:
            #     break

    open_words = set()
    for i, (_, _, word) in enumerate(words):
        if i not in prevent_spo_words:
            open_words.add(word)        

    # print(open_words)
    cnt = 0
    for i, (_, _, word) in enumerate(words):
        if i in prevent_spo_words:
            if word not in open_words:
                # print(word)
                cnt += 1
                open_words.add(word)
    
    answer = cnt
    return answer