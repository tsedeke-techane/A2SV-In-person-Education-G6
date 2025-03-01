# Problem: Books - https://codeforces.com/contest/279/problem/B

n = list(map(int, input().split()))  
p = list(map(int, input().split()))  

ans = 0  
window = 0  
left = 0  

for right in range(n[0]):  
    window += p[right]  

    while window > n[1] and left <= right:  
        window -= p[left]  
        left += 1  

    ans = max(ans, right - left + 1)  

print(ans)  
