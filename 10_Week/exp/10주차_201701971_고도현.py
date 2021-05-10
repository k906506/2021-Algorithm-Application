import sys

def main():
    n, m = input().split()
    n = int(n)
    m = int(m.replace(".", ""))

    item = []
    for i in range(n):
        price, calori = sys.stdin.readline().split()
        price = int(price.replace(".", ""))
        calori = int(calori)
        item.append((price, calori))


    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if item[i-1][0] > j: # 제품의 가격이 더 큰 경우
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-item[i-1][0]] + item[i-1][1])

    print(dp[n][m])

if __name__ == "__main__":
    main()