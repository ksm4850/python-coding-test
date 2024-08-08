import heapq

def solution(operations):
    answer = []
    for operation in operations:
        oper,num = map(str,operation.split(" "))

        if oper == "I":
            heapq.heappush(answer,int(num))    
        else:
            if num == "1":
                if len(answer) != 0:
                    answer.remove(max(answer))
            else:
                if len(answer) != 0:
                    heapq.heappop(answer)
    if answer:
        return [max(answer),answer[0]]
    else:
        return [0,0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))