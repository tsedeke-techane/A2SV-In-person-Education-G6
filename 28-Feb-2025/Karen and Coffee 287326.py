# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())

MAX_TEMP = 200000  

diff = [0] * (MAX_TEMP + 2)  

for _ in range(n):
    li, ri = map(int, input().split())
    diff[li] += 1  
    diff[ri + 1] -= 1  

t_count = [0] * (MAX_TEMP + 1)
running_sum = 0
for i in range(1, MAX_TEMP + 1):
    running_sum += diff[i]
    t_count[i] = running_sum  

admissible = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    if t_count[i] >= k:
        admissible[i] = 1  

prefix_sum = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    prefix_sum[i] = prefix_sum[i - 1] + admissible[i]

# Process queries
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])



