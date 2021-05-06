def findTime(people, times):
    minTime = 1
    maxTime = people * max(times) # 모든 고객들이 가장 느린 캐셔한테 간다고 가정

    while minTime <= maxTime:
        midTime = (minTime + maxTime)//2
        totalTime = 0
        for time in times:
            totalTime += midTime//time
            if totalTime >= people: # 시간이 넉넉한 경우 -> 줄인다
                result = midTime
                maxTime = midTime - 1
                break
        if totalTime < people: # 시간이 부족한 경우 -> 늘린다
            minTime = midTime + 1

    return result

def main():
    casher, people = map(int, input().split())
    times = list(map(int, input().split()))
    print(findTime(people, times))

if __name__ == "__main__":
    main()