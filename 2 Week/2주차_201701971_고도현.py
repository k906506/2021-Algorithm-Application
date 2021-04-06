import sys


def main():
    n = int(input())

    for _ in range(n):
        userInput = list(sys.stdin.readline())

        sum_input = 0
        plus = 1
        checkContinue = False

        element = userInput.pop(0)  # 입력된 문자열에서 첫번째 문자 pop
        while element != '\n':  # 문자가 개행문자일때까지 반복
            if element == 'A':  # 점수 부과 O
                if checkContinue:  # 이전 문자도 A였는지 확인
                    plus *= 2  # 이전 문자도 A인 경우 추가 점수
                sum_input += plus  # 점수 합산
                checkContinue = True
            else:  # 점수 부과 X
                checkContinue = False
                plus = 1
            element = userInput.pop(0)

        print(sum_input)  # 점수 합산


if __name__ == "__main__":
    main()
