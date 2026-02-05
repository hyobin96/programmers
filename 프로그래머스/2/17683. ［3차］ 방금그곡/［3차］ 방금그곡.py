# 시간초과 날 일은 없음
# 재생시간 계산해주는 함수
# C, C# 구분 필요 -> #이 붙은 걸 먼저 바꾸기
# 바꾸는 건 replace, 어차피 시간초과 넉넉함


def solution(m, musicinfos):
    
    def to_miniute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    def make_playtime_music(music, playtime):
        악보시간 = len(music)
        tmp = []
        if playtime <= 악보시간:
            music = music[:playtime]
        else:
            몫 = playtime // 악보시간
            나머지 = playtime % 악보시간
            music = music * 몫 + music[:나머지]
        return music
    
    mapping = {'A#': 'a', 'B#': 'b', 'C#': 'c', 'D#': 'd', 'E': 'e', 'F#': 'f', 'G#': 'g'}
    
    for key, value in mapping.items():
        m = m.replace(key, value)
    
    
    # 전처리
    for i, musicinfo in enumerate(musicinfos):
        musicinfos[i] = musicinfo.split(',')
        musicinfos[i][0], musicinfos[i][1] = to_miniute(musicinfos[i][0]), to_miniute(musicinfos[i][1])
        for key, value in mapping.items():
            musicinfos[i][3] = musicinfos[i][3].replace(key, value)
    
    # musicinfos.sort(key=lambda m: m[0])
    # print(musicinfos)

    answer = ("", 0)
    for i, musicinfo in enumerate(musicinfos):
        s, e = musicinfo[0], musicinfo[1]
        playtime = e - s
        playtime_music = make_playtime_music(musicinfo[3], playtime)
        if m in playtime_music:
            if answer[1] < playtime:
                answer = (musicinfo[2], playtime)
    
    return answer[0] if answer[0] else "(None)"