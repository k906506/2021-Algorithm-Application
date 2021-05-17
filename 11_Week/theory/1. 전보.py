import heapq
import sys

INF = float('inf')

def find(info, city, start):
    distance = [INF for _ in range(city+1)]
    distance[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    while queue:
        dist, current = heapq.heappop(queue) # 현재 노드까지의 거리, 현재 노드
        if distance[current] < dist: # 이미 최단 거리인 경우 패스
            continue
        for next in info[current]: # current와 연결된 다른 노드를 탐색
            if distance[next[0]] > distance[current] + next[1]:
                distance[next[0]] = distance[current] + next[1]
                heapq.heappush(queue, (distance[next[0]], next[0]))
    return distance

def main():
    city, comm, start = map(int, input().split())
    info = [[] for i in range(city+1)]

    for i in range(comm):
        src, dst, dist = map(int, sys.stdin.readline().split())
        info[src].append((dst, dist))

    distance = find(info, city, start)

    countCity = 0
    countTime = 0
    for i in range(1, len(distance)):
        if distance[i] != INF:
            countCity += 1
            countTime = max(countTime, distance[i])

    print(countCity-1, countTime) # 시작 노드 제외

if __name__ == "__main__":
    main()