import sys

def main():
    n = int(input())    # 사용하지 않아도 해결 가능
    numbers = list(sys.stdin.readline().split())     # 빠른 입력을 위해 sys.stdin.readline() 사용 & 문자열로 저장
    numbers = sorted(numbers, key = lambda x : x*3, reverse= True)      # 내림차순 정렬을 위한 reverse = True
    print("".join(numbers))     # .join으로 최종결과 출력

if __name__ == "__main__":
    main()