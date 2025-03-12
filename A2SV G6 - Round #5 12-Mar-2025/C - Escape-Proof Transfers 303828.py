# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
left = 0
for right in range(n):
    if arr[right] > t:
        left = right + 1
    if right - left + 1 >= c:
        count += 1
print(count)
