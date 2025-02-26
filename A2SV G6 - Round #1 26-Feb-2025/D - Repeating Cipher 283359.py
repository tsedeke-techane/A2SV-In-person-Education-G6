# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
words = input()

ans = []
index = 0
i = 1  

while index < n:  
    ans.append(words[index])
    index += i
    i += 1

print(''.join(ans))  
