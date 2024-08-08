a = 0

def dfs(i, result, numbers, target) :
    print(i, result)
    global a
    if i == len(numbers) : # i 현재 인덱스
        if result == target : 
            a+=1
            return
    else :
        dfs(i+1, result+numbers[i], numbers, target)
        dfs(i+1, result-numbers[i], numbers, target)

def solution(numbers, target):
    result = 0
    dfs(0, result, numbers, target)
    
    return a
print(solution([4, 1, 2, 1],4))