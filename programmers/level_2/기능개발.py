import math
def solution(progresses, speeds):
    # 작업소요일 계산
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0

    for idx in range(len(progresses)):

        if progresses[idx] > progresses[front]: # front가 현재 인덱스보다 크면
            answer.append(idx - front) # 이전 작업은 전부 동시출시
            front = idx  # 프론트 인덱스 현재 인덱스로 변경
    # 맨 마지막에 현재 프론트 인덱스와 전체 길이의 차를 구해서 남은 작업 다 출시
    answer.append(len(progresses) - front)  

    return answer

solution([93, 30, 55],[1, 30, 5])