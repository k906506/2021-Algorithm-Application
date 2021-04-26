import sys
from collections import deque

def groupIsland(map_list, src_x, src_y, n, groupId):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((src_x, src_y))

    map_list[src_x][src_y] = groupId # 시작 지점에 groupId 저장

    while queue:
        src_x, src_y = queue.popleft()
        for i in range(4):
            nx = src_x + dx[i]
            ny = src_y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n: # 주어진 범위 이내인 경우
                if map_list[nx][ny] == 1: # 땅인 경우
                    map_list[nx][ny] = groupId # groupId 저장
                    queue.append((nx, ny))
    return map_list

def findDistance(map_list, island, dist, id, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while island:
        src_x, src_y = island.popleft()
        for i in range(4):
            nx = src_x + dx[i]
            ny = src_y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if map_list[nx][ny] == 0 and dist[nx][ny] == -1: # 바다고 아직 땅이 확장되지 않은 경우
                    dist[nx][ny] = dist[src_x][src_y] + 1 # 해당 지점을 땅으로 바꿔준다
                    island.append((nx, ny))
                if map_list[nx][ny] < 0 and map_list[nx][ny] != id: # 다른 섬을 만난 경우 (= 다리 건설)
                    return dist[src_x][src_y]   # 값을 리턴한다

def main():
    n = int(input())

    map_list = [[] for _ in range(n)]

    for i in range(n):
        map_list[i] = list(map(int, sys.stdin.readline().split()))

    # 섬 별로 grouping
    groupId = -1
    for i in range(n):
        for j in range(n):
            if map_list[i][j] == 1:
                map_list = groupIsland(map_list, i, j, n, groupId)
                groupId -= 1

    # 최단 거리 탐색
    ans = sys.maxsize
    for id in range(-1, groupId, -1):
        island = deque()
        dist = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if map_list[i][j] == id:
                    island.append((i, j))
                    dist[i][j] = 0 # 0인 부분은 땅, -1인 부분은 바다
        ans = min(ans, findDistance(map_list, island, dist, id, n)) # 모든 섬에 대해 확장을 진행하고 최소 값 중 최소 값을 찾는다

    print(ans)

if __name__ == "__main__":
    main()
