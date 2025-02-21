# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

test= int(input())
for _ in range(test):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    def inb(x, y):
        return 0 <= x < n and 0 <= y < m

    ans = []
    for i in range(n):
        for j in range(m):
            s = -3 * mat[i][j]
            for dx, dy in dirs:
                x, y = i, j
                while inb(x, y):
                    s += mat[x][y]
                    x, y = x + dx, y + dy
            ans.append(s)
    print(max(ans))