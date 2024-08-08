def solution(routes):
    # 종료 지점 기준으로 경로를 정렬
    routes.sort(key=lambda x: x[1])
    
    # 첫 번째 카메라를 첫 번째 경로의 종료 지점에 설치
    cameras = 0
    current_camera = -30001
    
    for route in routes:
        # 현재 카메라가 다음 차량의 경로와 겹치지 않는다면
        if current_camera < route[0]:
            cameras += 1
            current_camera = route[1]
    
    return cameras

# 예제 테스트 케이스
routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))  # Output: 2