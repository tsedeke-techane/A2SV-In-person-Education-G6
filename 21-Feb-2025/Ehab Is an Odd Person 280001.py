# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
arr = list(map(int, input().split()))

oddNum = sum(1 for x in arr if x % 2 != 0)
evenNum = n - oddNum

if oddNum == 0 or evenNum == 0:
    print(" ".join(map(str, arr)))
else:
    arr.sort()
    print(" ".join(map(str, arr)))

