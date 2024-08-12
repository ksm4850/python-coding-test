import json
def solution(s:str):
    answer = []
    s = s.replace("{","[").replace("}","]")
    s = json.loads(s)
    s.sort(key=len)
    for arr in s:
        for a in arr:
            if not a in answer:
                answer.append(a)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))


import re
from collections import Counter
def solution(s):
    print(re.findall('\d+', s))
    s = Counter(re.findall('\d+', s)) 
    # 정규식 re.findall('\d+', s)은 문자열 s에서 숫자들로 이루어진 모든 부분을 찾음
    # "{{2},{2,1},{2,1,3},{2,1,3,4}}" -> ['2', '2', '1', '2', '1', '3', '2', '1', '3', '4']
    # Counter로 추출된 숫자의 빈도를 계산

    # 빈도수 많은 순서대로 배열 return
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
