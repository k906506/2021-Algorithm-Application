def findDirection(directInfoDict, cnt, direction):
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index = dir.index(direction)
    try:
        if directInfoDict[cnt] == 'R': # R인 경우
            if index == 3: # dir가 연결되어있다고 생각.
                index = 0
            else:
                index += 1
        else: # L인 경우
            if index == 0: # dir가 연결되어있다고 생각.
                index = 3
            else:
                index -= 1
        return dir[index]
    except: # directInfoDict[cnt] 값이 없는 경우 기존 진행 방향 return
        return direction


def main():
    n = int(input())
    apple = int(input())
    turn = int(input())
    worm = list()

    map_info = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(apple):
        x, y = map(int, input().split())
        map_info[x-1][y-1] = 1

    directInfoDict = dict()
    for i in range(turn):
        cnt, direct = input().split()
        cnt = int(cnt)
        directInfoDict[cnt] = direct

    direction = (0, 1) # Default 방향성 (우측)
    cnt = 0
    i = 0
    j = 0
    length = 1
    worm.append((0, 0)) # 시작 지점
    while True:
        direction = findDirection(directInfoDict, cnt, direction) # 진행 방향 판단.
        i += direction[0] # 다음 좌표.
        j += direction[1] # 다음 좌표.
        cnt += 1 # 이동 횟수 count.
        if i < 0 or i >= n or j < 0 or j >= n: # 정사각형을 벗어나면 종료.
            break
        if length >= 5 and (i, j) in worm:  # 자기 자신과 겹치면 종료.
            break
        if map_info[i][j] == 1: # 사과를 먹으면 길이 +1.
            worm.append((i, j))
            length += 1
        else:
            worm.pop(0) # 사과를 먹지 않은 경우 과거의 위치를 제거하고 현재 위치 추가.
            worm.append((i, j))

    print(cnt) # 이동 횟수 print

if __name__ == "__main__":
    main()
