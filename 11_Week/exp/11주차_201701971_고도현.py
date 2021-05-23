import sys
INF = float('inf')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = ['U', 'D', 'L', 'R']

def find(maps, m, n):
    visited = [[INF for _ in range(n)] for _ in range(m)] # 변경이 필요한 개수를 저장할 배열
    visited[0][0] = 0 # 초기 위치는 변경횟수 0
    ans = INF

    queue = [(0, 0, 0)]

    while queue:
        x, y, cnt = queue.pop(0)
        if x == m-1 and y == n-1:
            ans = min(ans, cnt)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            next_dir = direction[i]
            new_cnt = cnt
            if nx >= 0 and nx < m and ny >= 0 and ny < n: # 범위 이내인 경우
                if maps[x][y] != next_dir: # 방향성이 다르면
                    new_cnt += 1
                if visited[nx][ny] > new_cnt: # 방문하려는 좌표의 변경 횟수가 더 크면
                    visited[nx][ny] = new_cnt
                    queue.append((nx, ny, new_cnt))

    return ans

def main():
    m, n = map(int, input().split())
    maps = [[] for _ in range(m)]

    for i in range(m):
        maps[i] = list(sys.stdin.readline().split())

    print(find(maps, m, n))


if __name__ == "__main__":
    main()