def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])


def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a > parent_b:  # b가 더 높은 부모
        parent[a] = b

    elif parent_a < parent_b:
        parent[b] = a


def main():
    n, m = map(int, input().split())
    # 부모를 비교해서 부모가 같은 경우 사이클 발생한 것


if __name__ == "__main__":
    main()
