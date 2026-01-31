# uid: 닉네임
# q에 (1, uid) 넣기 , 1은 Enter, 2 은 Leave, 3는 Change, 미리 매핑
# 1과 2일때만 넣기, 3일때는 uid: 닉네임 변경
# 다 넣고 꺼내면서 result 채우기
# 

def solution(record):
    uid_nickname = dict()
    행동_dict = {"Enter": 1, "Leave": 2, "Change": 3}
    message_dict = {1: "들어왔습니다.", 2: "나갔습니다."}
    
    l = []
    for r in record:
        r = r.split()
        행동 = 행동_dict[r[0]]
        
        if 행동 == 1:
            uid, nickname = r[1], r[2]
            uid_nickname[uid] = nickname
            l.append((행동, uid))
        elif 행동 == 2:
            uid = r[1]
            l.append((행동, uid))
        else:
            uid, nickname = r[1], r[2]
            uid_nickname[uid] = nickname
        
    result = []
    for 행동, uid in l:
        nickname = uid_nickname[uid]
        message = message_dict[행동]
        result.append(nickname + "님이 " + message)
    
    return result