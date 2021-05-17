import sys
INF = float('inf')

def find(n, times, x, y):
    for i in range(1, n+1):
        times[i][i] = 0 # 자기 자신에 대한 거리는 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    distance = times[1][y] + times[y][x]

    if distance == INF:
        return -1
    else:
        return distance

def main():
    n, m = map(int, input().split())
    times = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        src, dst = map(int, sys.stdin.readline().split())
        times[src][dst] = 1
        times[dst][src] = 1

    x, y = map(int, input().split())
    print(find(n, times, x, y))

if __name__ == "__main__":
    main()