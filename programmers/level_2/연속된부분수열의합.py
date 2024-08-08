def solution(sequence, k):
    
    answer = [0, len(sequence)]
    l = r = 0
    sum = sequence[0]
    while True:
        if sum < k: # 합이 k보다 작으면
            r += 1
            if r == len(sequence): break
            sum += sequence[r]
        else:
            if sum == k:
                if r-l < answer[1] - answer[0]:
                    answer = [l,r]
            sum -= sequence[l]
            l += 1
    return answer

print([1, 2, 3, 4, 5],7)