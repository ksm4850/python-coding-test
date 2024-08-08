
def solution(keymap, targets):
    answer = []
    for target in targets:
        times = 0
        for char in target:
            flag = False
            time = 101
            for key in keymap:
                if char in key:
                    time = min(key.index(char)+1, time)
                    flag = True
            if not flag:
                times = -1
                break
            times += time
        answer.append(times)
    return answer

# print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))