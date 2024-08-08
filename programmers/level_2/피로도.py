from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0 
        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer
# 최소피로도
# 소모피로도
print(80,[[80,20],[50,40],[30,10]])