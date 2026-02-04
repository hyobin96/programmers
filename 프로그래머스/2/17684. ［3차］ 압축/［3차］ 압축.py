# 시간초과는 안 남

def solution(msg):
    dictionary = {}
    # print(ord('A')) 65
    
    for i in range(26):
        dictionary[chr(65 + i)] = i + 1 
    
        
    answer = []
    idx = 0
    글자 = msg
    while True:
        if 글자 in dictionary:
            answer.append(dictionary[글자])
            if 글자 == msg:
                dictionary[글자] = len(dictionary) + 1
                break
                
            dictionary[글자 + msg[-idx]] = len(dictionary) + 1
            msg = msg[-idx : ]
            글자 = msg
            idx = 0
            continue
        
        idx += 1
        글자 = msg[ : -idx]
    
    return answer