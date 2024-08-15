def solution(word):
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt+1, w + words[i])
            
    dfs(0,"") # dfs를 이용해 모든 단어를 배열에 저장
    # 찾을 단어 인덱스 + 1 해서 리턴
    return word_list.index(word)+1

print(solution('AE'))


# def solution(word):
#     answer = 0
#     arr = ['A', 'E', 'I', 'O', 'U']
#     num = [781, 156, 31, 6, 1]
#     for i in range(len(word)):
#         answer += arr.index(word[i]) * num[i] + 1
#     return answer