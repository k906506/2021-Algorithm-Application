import random
import sys

def main():
    n = int(input())
    score = []

    count = 1
    while count <= n:
        i = random.randint(1, n)
        if i not in score:
            score.append(i)
            count += 1

    sys.stdout = open('test.txt', 'w')

    for i in range(n):
        print(score[i], end = " ")

if __name__ == "__main__":
    main()