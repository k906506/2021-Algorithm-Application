INF = float('inf')

def main():
    n, m = map(int, input().split())

    maps = [[] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = [[INF for _ in range(m)] for _ in range(n)]

    for i in range(n):
        maps[i] = list(map(int, input().split()))

    sortedMaps = []
    for i in range(n):
        for j in range(m):
            sortedMaps.append((maps[i][j], i, j))

    sortedMaps.sort() # 오름차순으로 정렬

    while sortedMaps: # 가장 작은 원소부터 순서를 정해준다
        value, row, col = sortedMaps.pop(0)
        if visited[row][col] == False: # 아직 방문하지 않은 경우
            elements = [] # 해당 row, col에 더 작은 원소의 개수를 세기 위한 리스트
            indexs = [] # 더 작은 원소의 index를 담기 위한 리스트
            for k in range(n):  # 0 ~ n-1까지 탐색
                if k == row:  # 기준점의 row과 같은 경우
                    for l in range(m):  # 해당 row의 모든 col을 비교한다.
                        if value > maps[k][l]: # 더 작은 원소가 있는 경우
                            elements.append(maps[k][l]) # 더 작은 원소를 저장한다.
                            indexs.append(result[k][l]) # 더 작은 원소의 index를 저장한다.
                else:  # 기준점의 row와 다른 경우
                    if value > maps[k][col]:
                        elements.append(maps[k][col])
                        indexs.append(result[k][col])

            if len(elements) == 0: # 해당 원소가 가장 작은 경우 elements 리스트에는 아무 원소도 없다.
                result[row][col] = 1 # 따라서 rank는 1
            else: # 그렇지 않은 경우
                rank = max(indexs) # 더 작은 원소들 중에서 가장 큰 원소의 rank에서 1을 더해준다.
                result[row][col] = rank + 1

            visited[row][col] = True # 해당 정점 방문 처리

    for i in range(n):
        print(*result[i])

if __name__ == "__main__":
    main()