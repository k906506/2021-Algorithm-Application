def main():
    move = input()
    loc_col = int(ord(move[0])) - int(ord('a'))
    loc_row = int(move[1]) - 1

    dx = (-2, -1, 1, 2, -2, -1, 1, 2)
    dy = (-1, -2, -2, -1, 1, 2, 2, 1)

    count = 0
    for i in range(8):
        nx = loc_col + dx[i]
        ny = loc_row + dy[i]
        if nx >= 0 and nx < 8 and ny >=0 and ny < 8:
            count += 1

    print(count)

if __name__ == "__main__":
    main()

