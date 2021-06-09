def find(ice, x, y, n, m):
    ice[x][y] = 1
    cnt = 0
    queue = []
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        element = queue.pop(0)
        for i in range(4):
            nx = element[0] + dx[i]
            ny = element[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                ice[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny))

    return cnt

def main():
    n, m = map(int, input().split())
    ice = [[] for _ in range(n)]

    for i in range(n):
        ice[i] = list(map(int, input()))

    result = []
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                result.append(find(ice, i, j, n, m))

    print(result)

if __name__ == "__main__":
    main()