def solution(scores):
    완호 = scores[0]
    
    scores.sort(reverse=True)
    
    new_scores = [scores[0]]
    # print(new_scores)
    prev = new_scores[0]
    curr = new_scores[0]
    for i in range(1, len(scores)):
        # print(prev, curr)
        score = scores[i]
        if score[0] < curr[0]:
            prev = curr
            
        if score[0] < prev[0] and score[1] < prev[1]:
            continue
            
        if score[0] < curr[0] and score[1] > prev[1]:
            curr = score
             
        new_scores.append(score)
    
    new_scores.sort(key=lambda s: -(s[0] + s[1]))
    
    # print(new_scores)
    
    rank = 1
    answer = -1
    prev = new_scores[0][0] + new_scores[0][1]
    # print(new_scores)
    for i, (a, b) in enumerate(new_scores):
        if prev != (a + b):
            rank = i + 1
            prev = a + b
            
        if a == 완호[0] and b == 완호[1]:
            answer = rank
            break
    
    return answer