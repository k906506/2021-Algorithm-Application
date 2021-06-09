def find(items, m, begin, end):
    ans = 0
    while begin <= end:
        mid = (begin + end) // 2
        sum = 0
        for element in items:
            if element > mid:
                sum += element - mid
        if sum >= m:  # 더 많이 잘라야함
            begin = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


def main():
    n, m = map(int, input().split())
    items = list(map(int, input().split()))

    print(find(items, m, 0, max(items)))


if __name__ == "__main__":
    main()
