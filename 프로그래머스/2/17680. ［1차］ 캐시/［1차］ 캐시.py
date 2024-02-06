# 2018 KAKAO BLIND RECRUITMENT

"""
    조건:
        - cacheSize 는 30
        - cities 는 10만, 대소문자 구분없는 영문
        - LRU 알고리즘 -> 최근 hit 된것들 순으로 보관
    구현:
        - cache = [], cacheSize == len(cache) 때 마다 쓰이지 않은 것 삭제
        - 다시 hit 된 city 는 배열 끝으로 이동
"""

def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.remove(cache[0])
        
        
    return time