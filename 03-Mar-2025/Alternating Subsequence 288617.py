# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    max_num = arr[0]

    for i in range(1, n):
        if (arr[i] > 0 and max_num > 0) or (arr[i] < 0 and max_num < 0):
            max_num = max(arr[i], max_num)
        else:
            ans += max_num
            max_num = arr[i]

    ans += max_num
    print(ans)