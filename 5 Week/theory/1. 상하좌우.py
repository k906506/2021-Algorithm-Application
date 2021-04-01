def main():
    n = int(input())
    command = list(input().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    move = ['L', 'R', 'D', 'U']
    x = 0
    y = 0

    for direct in command:
        i = move.index(direct)
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        x = nx
        y = ny
    print(y, x)

if __name__ == "__main__":
    main()