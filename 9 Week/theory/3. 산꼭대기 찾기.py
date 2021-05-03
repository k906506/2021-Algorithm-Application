def binary(mountain):
    high = len(mountain) - 1
    low = 0

    while low < high:
        mid = (low + high) // 2
        if mountain[mid] < mountain[mid+1]:
            low = mid + 1
        else:
            high = mid
    return low


def main():
    mountain = list(map(int, input().split()))
    print(binary(mountain))

if __name__ == "__main__":
    main()