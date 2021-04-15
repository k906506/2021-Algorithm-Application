def dfs(ice, n, m, x, y, count):
    ice[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if ice[nx][ny] == 0:
                count = dfs(ice, n, m, nx, ny, count+1)
    return count

def main():
    n, m = map(int, input().split()) # row, col
    ice = [[] for _ in range(n)]

    for i in range(n):
        ice[i] = list(map(int, input()))

    result = []

    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                result.append(dfs(ice, n, m, i, j, 1)) # 얼음을 얼릴 수 있는 영역까지 얼린다. 얼음의 크기가 리턴.

    print(result) # 얼려진 얼음의 크기가 담겨있다.

if __name__ == "__main__":
    main()