def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        # 해당위치 값 = max(해당위치 // n , 해당위치 % n) +1
        answer.append(max(i // n, i % n) + 1)

    return answer