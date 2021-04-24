import time
import sys

def selectSort(input_list): # 선택정렬
    for i in range(len(input_list)):
        min_index = i
        for j in range(i, len(input_list)):
            if input_list[j] <= input_list[min_index]: # 오름차순
                min_index = j

        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
        ''' 파이썬의 Swap 방법, 풀어쓰면 아래와 같다.
        temp = input_list[i]
        input_list[i] = input_list[min_index]
        input_list[min_index] = temp
        '''


def insertSort(input_list):
    for i in range(1, len(input_list)):
        for j in range(i, 0, -1):
            if input_list[j] <= input_list[j-1]:
                input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
            else:
                break


def quickSort(input_list, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and input_list[left] <= input_list[pivot]: # pivot보다 큰 원소를 찾는다
            left += 1
        while right > start and input_list[right] >= input_list[pivot]: # pivot보다 작은 원소를 찾는다
            right -= 1
        if left > right: # 엇갈린 경우
            input_list[pivot], input_list[right] = input_list[right], input_list[pivot]
        else:
            input_list[left], input_list[right] = input_list[right], input_list[left]

    quickSort(input_list, start, right-1)
    quickSort(input_list, right+1, end)

def countSort(input_list):
    count_list = [0 for _ in range(len(input_list))]

    for i in range(len(input_list)):
        count_list[input_list[i]-1] += 1

    '''
    for i in range(len(count_list)):
        if count_list[i] != 0:
            for j in range(count_list[i]):
                print(i+1, end = " ")
    '''

def main():
    input_list = list(map(int, input().split()))

    # 선택정렬 시간 측정
    start = time.time()
    selectSort(input_list)
    end = time.time() - start
    print("선택정렬 : %f" %end)


    # 삽입정렬 시간 측정
    start = time.time()
    insertSort(input_list)
    end = time.time() - start
    print("삽입정렬 : %f" %end)

    # 퀵정렬 시간 측정
    start = time.time()
    quickSort(input_list, 0, len(input_list)-1)
    end = time.time() - start
    print("퀵정렬 : %f" %end)

    # 계수정렬 시간 측정
    start = time.time()
    countSort(input_list)
    end = time.time() - start
    print("계수정렬 : %f" %end)

if __name__ == "__main__":
    sys.setrecursionlimit(1000000000)
    main()