from collections import deque


def bfs(maze, visited, n, m):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0: # 다음 좌표가 길인 경우
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny)) # 다음 좌표를 queue에 삽입.


def main():
    n, m = map(int, input().split())  # row, col
    maze = [[] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        maze[i] = list(map(int, input()))

    print(bfs(maze, visited, n, m))

if __name__ == "__main__":
    main()


