import heapq


def prim(infos, n, m):
    queue = []
    visited = [False for _ in range(n + 1)]
    ans = 0

    heapq.heappush(queue, [0, 1])  # dist, src

    while queue:
        dist, src = heapq.heappop(queue)
        if visited[src]:
            continue
        for dst, value in infos[src]:
            heapq.heappush(queue, [value, dst])
        ans += dist
        visited[src] = True

    return ans


def main():
    n, m = map(int, input().split())
    infos = [[] for _ in range(n + 1)]
    for _ in range(m):
        src, dst, value = map(int, input().split())
        infos[src].append([dst, value])
        infos[dst].append([src, value])

    print(prim(infos, n, m))


if __name__ == "__main__":
    main()
