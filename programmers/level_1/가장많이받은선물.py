def solution(friends, gifts):
    answer = 0

    gifted = {} # {준사람 : { 받은사람 : 갯수}}
    gift_idx = {} # 선물지수 {이름 : 지수}
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0
    
    for gift in gifts:
        g,t = gift.split(' ')
        if t in gifted[g]:
            gifted[g][t] += 1
        else:
            gifted[g][t] = 1

        gift_idx[g] += 1
        gift_idx[t] -= 1

    # 받을선물갯수 
    will_get = [ 0 for _ in friends]
    for i in range(len(friends)):
        curr = friends[i] 
        for j in range(i+1,len(friends)):
            
            another = friends[j] 
            
            # curr이 another에게 준 선물갯수
            a = gifted[curr][another] if another in gifted[curr] else 0
            # another가 curr에게 준 선물갯수
            b = gifted[another][curr] if curr in gifted[another] else 0

            if a > b:
                will_get[i] += 1
            elif a < b:
                will_get[j] += 1
            elif a == b:
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1
    answer = max(will_get)    
    return answer


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends,gifts))