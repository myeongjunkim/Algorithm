# 2018 KAKAO BLIND RECRUITMENT [1차] 캐시

def solution(cacheSize, cities):
    cache=[]
    time = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            if cacheSize !=0:
                if len(cache) == cacheSize:
                    oldest_city = cache[0]
                    cache.remove(oldest_city)
                cache.append(city)
return time