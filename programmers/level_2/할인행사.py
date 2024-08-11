from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number): # {품목 : 수량} 변환 
        check[w] = n
    
    for i in range(len(discount)-9): # 10일씩 확인
        c = Counter(discount[i:i+10]) # 10일간의 품목 {품목 : 수량} 변환 
        if c == check: # 같다면 + 1
            answer += 1

    # # Counter 안쓰고 구현
    # for i in range(len(discount)-9): # 10일씩 확인
    #     d = {}
    #     for j in discount[i:10+i]:
    #         if d in j:
    #             d[j] += 1
    #         else:
    #             d[j] = 1
    
    return answer