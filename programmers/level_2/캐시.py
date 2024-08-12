# cache hit = 1
# cache miss = 5 

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower() # 대소문자 구분 x
        if cacheSize: # 캐시사이즈가 0이 아니면
            if city in cache: # 캐시가 존재하면
                # 가장 최근에 참조회었다는 의미이므로 기존에 있던 캐시 삭제후 맨뒤에 다시 저장
                cache.pop(cache.index(city)) 
                cache.append(city)
                answer += 1
            else:
                if len(cache) == cacheSize: # 캐시사이즈가 최대라면 처음들어온 데이터 삭제
                    cache.pop(0)
                cache.append(city)
                answer += 5
        else:  # 캐시사이즈가 0이면 +5
            answer += 5
    return answer

print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))