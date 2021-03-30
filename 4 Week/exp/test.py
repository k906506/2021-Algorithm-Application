import random
import sys

def main():
    n = int(input())
    score = [[0, 0] for _ in range(n)]

    count = 1
    num = []
    while count <= n:
        i = random.randint(1, n)
        if i not in num:
            num.append(i)
            count += 1

    for i in range(n):
        score[i][0] = num[i]

    count = 1
    num = []
    while count <= n:
        i = random.randint(1, n)
        if i not in num:
            num.append(i)
            count += 1

    for i in range(n):
        score[i][1] = num[i]

    sys.stdout = open('test.txt', 'w')

    for i in range(n):
        print(score[i][0], score[i][1])

if __name__ == "__main__":
    main()