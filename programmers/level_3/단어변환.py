from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [False] * len(words)

    while q:
        word,cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]: # 방문안한 단어면
                for j in range(len(word)):
                    if word[j] != words[i][j]:# 한글자씩 비교
                        temp_cnt += 1
                if temp_cnt == 1: # 한글자만 바뀐경우
                    q.append([words[i], cnt + 1])
                    visited[i] = True
                    
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))