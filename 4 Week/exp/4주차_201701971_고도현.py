import sys

def main():
    n = int(input())

    score = [[] for _ in range(n)]
    for i in range(n):
        score[i] = list(map(int, sys.stdin.readline().split())) # 빠른 입력을 위한 stdin.readline.

    score = sorted(score, key = lambda x : x[0])    # 등수의 중복이 없으므로 한 과목만을 기준으로 잡아도 Ok.

    firstSubGrade = score[0][0]
    secondSubGrade = score[0][1]
    result = 1

    for i in range(1, len(score)):
        if score[i][0] > firstSubGrade and score[i][1] < secondSubGrade:    # 첫 번째 과목의 둥수가 1등보다 낮지만 두 번째 과목의 등수가 1등보다 높으면 count.
            firstSubGrade = score[i][0]
            secondSubGrade = score[i][1]   # 기준을 다시 잡는다.
            result += 1

    print(result)

if __name__ == "__main__":
    main()