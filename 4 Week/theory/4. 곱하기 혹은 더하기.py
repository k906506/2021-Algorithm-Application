def main():
    string = input()

    result = 0
    for i in range(len(string)):
        num = int(string[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

    print(result)

if __name__ == "__main__":
    main()