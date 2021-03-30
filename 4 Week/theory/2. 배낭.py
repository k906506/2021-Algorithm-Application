def main():
    n, max_weight = map(int, input().split())
    price = list()

    for i in range(n):
        price.append(list(map(int, input().split())))   # 가치, 무게

    back = list()
    for e in price:
        back.append((e[0]/e[1], e[0], e[1]))
    back.sort(reverse = True)

    result : float = 0
    for e in back:
        if max_weight - e[2] >= 0:
            max_weight -= e[2]
            result += e[1]
        else:
            result += e[1] * (max_weight / e[2])
            break

    print(result)

if __name__ == "__main__":
    main()