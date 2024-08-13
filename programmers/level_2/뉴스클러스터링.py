from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower() # 소문자로 변경

    # for i in range(len(str1)-1):
    #     s:str = str1[i:i+2]
    #     if s.isalpha():
    #         str1_lst.append(s)

    # for i in range(len(str2)-1):
    #     s:str = str2[i:i+2]
    #     if s.isalpha():
    #         str2_lst.append(s)

    # 리스트컴프리핸션으로 한줄로 표현
    # 다중집합 구하기
    str1_lst = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_lst = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    # Counter 메서드도 set()과 마찬가지로 집합 구조를 생성할 수 있다
    # 교집합 &, 합집합 | 
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    # 자카드 유사도 구하기
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

print(solution("FRANCE","french"))