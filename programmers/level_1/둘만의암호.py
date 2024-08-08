def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    # 스킵할 문자 제거
    for i in list(skip):
        alpha = alpha.replace(i,"")
    
    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]
    return answer

print(solution("aukks","wbqd",5))