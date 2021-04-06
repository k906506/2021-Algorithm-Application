from itertools import permutations
import math


def prime_num(prime_list, number):

    for i in range(2, int(math.sqrt(number)) + 1): # 빠른 탐색을 위해 제곱근까지만 탐색한다.
        if prime_list[i] == 0: # i가 소수인 경우 다음 수로 넘어간다.
            continue
        for j in range(i + i, number + 1, i): # i의 배수들은 소수가 아니다.
            prime_list[j] = 0

    return prime_list


def main():
    string = input()
    element = list()
    ans = 0

    # 모든 경우의 수를 탐색하고 이를 숫자문자열로 변환한다.
    for i in range(1, len(string) + 1):
        p = list(permutations(string, i))
        for j in range(len(p)):
            element.append(int("".join(p[j])))

    # 중복을 제거하고 다시 리스트로 변환 후 오름차순으로 정렬한다.
    element = set(element)
    element = list(element)
    element.sort()

    max_value = max(element)

    # 숫자를 저장할 배열을 만든다.
    prime = [1 for _ in range((max_value) + 1)]
    prime[0] = 0 # 0 과 1은 소수가 아니다.
    prime[1] = 0
    prime = prime_num(prime, max_value)

    for e in element:
        if prime[e]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
