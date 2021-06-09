def selectSort(numbers):  # 순회하면서 가장 작은 원소랑 위치 변경
    print("[선택 정렬] 정렬 전 : ", str(numbers))

    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        # numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp

    print("[선택 정렬] 정렬 후 : ", str(numbers))
    print("")


def insertSort(numbers):  # 순회하면서 이전 원소와 크기 비교
    print("[삽입 정렬] 정렬 전 : ", str(numbers))

    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j - 1]:
                temp = numbers[j - 1]
                numbers[j - 1] = numbers[j]
                numbers[j] = temp
            else:  # 이전 값이 더 작으면 순회 필요 없음.
                break

    print("[삽입 정렬] 정렬 후 : ", str(numbers))
    print("")


def quickSort(numbers, start, finish):
    if start >= finish:
        return
    pivot = start
    left = start + 1
    right = finish
    while left <= right:
        while left <= finish and numbers[left] <= numbers[pivot]:
            left += 1
        while right >= start and numbers[right] >= numbers[pivot]:
            right -= 1
        if left > right:
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    quickSort(numbers, start, right - 1)
    quickSort(numbers, right + 1, finish)



def main():
    numbers = list(map(int, input().split()))
    another_numbers = numbers.copy()
    selectSort(another_numbers)

    another_numbers = numbers.copy()
    insertSort(another_numbers)

    another_numbers = numbers.copy()
    quickSort(another_numbers, 0, len(numbers) - 1)


if __name__ == "__main__":
    main()
