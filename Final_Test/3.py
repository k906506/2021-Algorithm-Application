def selectSort(numbers): # 순회하면서 가장 작은 원소랑 위치 변경
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


def insertSort(numbers): # 순회하면서 이전 원소와 위치 변경
    print("[삽입 정렬] 정렬 전 : ", str(numbers))

    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j - 1]:
                temp = numbers[j - 1]
                numbers[j - 1] = numbers[j]
                numbers[j] = temp
            else:
                break

    print("[삽입 정렬] 정렬 후 : ", str(numbers))


def main():
    numbers = list(map(int, input().split()))
    another_numbers = numbers.copy()
    selectSort(another_numbers)

    another_numbers = numbers.copy()
    insertSort(another_numbers)


if __name__ == "__main__":
    main()
