# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n-1:
        if nums[i] > nums[i+1]:
            ans += 1
            i += 1
        i += 1
    print(ans)