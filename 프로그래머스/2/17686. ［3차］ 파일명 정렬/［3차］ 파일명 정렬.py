# files 쪼개기
# lower 
 
import re

def solution(files):
    # 괄호 사용 시 구분 문자열 포함
    for i, file in enumerate(files):
        files[i] = re.split(r'([0-9]+)', file)
        
    files.sort(key=lambda f: (f[0].lower(), int(f[1])))
    
    for i, file in enumerate(files):
        files[i] = ''.join(file)
        
    return files