def binary(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        result = (mid * (mid + 1)) // 2
        if result == n:
            return result
        if n < result: # 범위를 줄여야 함
            right = mid - 1
        else: # 범위를 넓여야 함
            left = mid + 1
    return right

def main():
    n = int(input())
    print(binary(n))

if __name__ == "__main__":
    main()
