def solution(clothes):
    # 각 종류별 가진 의상을 저장 (종류:[이름, 이름, ...])
    closet = {}
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]

    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    # (N+1)(M+1) = NM + N + M + 1
    # 1은 모두 사용하지않는경우
    answer = 1
    for _, value in closet.items():
        answer *= len(value) + 1
    # 1을 뺀 값 리턴
    return answer - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)
