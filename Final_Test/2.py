from collections import deque


def find(maps, paths, n, m):
    queue = deque()
    queue.append((0, 0))
    paths[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        element = queue.popleft()
        for i in range(4):
            nx = element[0] + dx[i]
            ny = element[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and paths[nx][ny] == 0:
                paths[nx][ny] = paths[element[0]][element[1]] + 1
                queue.append((nx, ny))

    return paths[n - 1][m - 1]


def main():
    n, m = map(int, input().split())
    maps = [[] for _ in range(n)]
    paths = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        maps[i] = list(map(int, input()))

    print(find(maps, paths, n, m))


if __name__ == "__main__":
    main()
