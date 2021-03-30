def main():
    n = int(input())
    scare = list(map(int, input().split()))
    scare.sort()

    result = 0
    count = 0

    for i in scare:
        count += 1
        if count >= i:
            result += 1
            count = 0

    print(result)

if __name__ == "__main__":
    main()