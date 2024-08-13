from collections import deque
def solution(priorities, location):
    answer = 0

    queue = deque([(i,p) for i,p in enumerate(priorities)])

    while True:
        cur = queue.popleft() # 대기중인 프로세스 하나 꺼냄
        # any() iterable한 객체에 하나라도 참이면 True
        if any(cur[1] < q[1] for q in queue): # 우선순위가 높은 프로세스가 있다면 
            queue.append(cur) # 다시 넣음
        else:
            answer += 1 # 우선순위가 가장 높다면 +1
            if cur[0] == location: # 현재 값이 location 값이면 return
                return answer