
def timeToDay(day):
    y, m, d = map(int, day.split('.'))
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    term = {i.split()[0]: int(i.split()[1]) for i in terms}
    today = timeToDay(today)

    for idx, p in enumerate(privacies):
        start_day, kind = p.split()
        if timeToDay(start_day) + term[kind] * 28 <= today:
            answer.append(idx+1)

    return answer

print(solution("2022.05.19",
      ["A 6", "B 12", "C 3"],
      ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))