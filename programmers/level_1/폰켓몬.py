def solution(nums):
    answer = 0
    n = len(nums) // 2
    s = len(set(nums))

    return min(n, s)


print(solution([3, 3, 3, 2, 2, 2]))
