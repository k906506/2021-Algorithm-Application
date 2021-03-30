def main():
    price = int(input())
    coins = list(map(int, input().split()))

    coins.sort(reverse = True)

    result = 0
    for coin in coins:
        result += price//coin
        price %= coin

    print(result)

if __name__ == "__main__":
    main()