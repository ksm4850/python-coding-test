def solution(dirs):
    answer = set()
    # 문자별 이동 좌표
    loc = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    x, y = 0,0 # 시작위치
    for d in dirs:
        dx, dy = loc[d]
        nx, ny = x + dx, y + dy # 이동할곳

        if abs(nx) <= 5 and abs(ny) <= 5: # -5 ~ 5 사이만 이동하게 조건
            answer.add(((y, x),(ny, nx))) # 기존좌표, 이동좌표
            answer.add(((ny, nx),(y, x))) # 이동좌표, 기존좌표
            y = ny
            x = nx

    return len(answer) // 2