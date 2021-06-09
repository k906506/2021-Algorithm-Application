def bisect_left(arr, value, begin, end):
    if begin >= end:
        return begin
    mid = (begin + end) // 2
    if arr[mid] < value:
        return bisect_left(arr, value, mid + 1, end)
    else:
        return bisect_left(arr, value, begin, mid)


def bisect_right(arr, value, begin, end):
    if begin >= end:
        return begin
    mid = (begin + end) // 2
    if value < arr[mid]:
        return bisect_right(arr, value, begin, mid)
    else:
        return bisect_right(arr, value, mid + 1, end)


def main():
    numbers = [1, 1, 2, 3, 4, 5, 5, 6]
    print(bisect_left(numbers, 5, 0, len(numbers)))
    print(bisect_right(numbers, 5, 0, len(numbers)))


if __name__ == "__main__":
    main()
