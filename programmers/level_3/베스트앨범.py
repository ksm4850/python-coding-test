# def solution(genres, plays):
#     answer = []
#     dic = {}

#     for g, p in zip(genres, plays):
#         if g not in dic.keys():
#             dic[g] = [p]
#         else:
#             dic[g] += [p]
#     print(dic)
#     max = 0
#     max_genres = ''
#     for k,v in dic.items():
#         if sum(v) < max:
#             max = sum(v)
#             max_genres = k

#     return answer


def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for k, v in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for i, p in sorted(dic1[k], key=lambda x: (x[1], -x[0]), reverse=True)[:2]:
            answer.append(i)

    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500]
    )
)
