def cutting(item, n, m, max_item, min_item):
    result = 0
    while min_item <= max_item:
        total = 0
        mid = (max_item + min_item) // 2
        for e in item:
            if e > mid:
                total += (e-mid)
        if total < m: # 덜 잘라야함 -> mid를 줄여야함
            max_item = mid - 1
        else: # 더 잘라야함 -> mid를 늘려야함
            result = mid
            min_item = mid + 1

    return result

def main():
    n, m = map(int, input().split())
    item = list(map(int, input().split()))

    max_item = max(item)
    min_item = 0
    print(cutting(item, n, m, max_item, min_item))

if __name__ == "__main__":
    main()