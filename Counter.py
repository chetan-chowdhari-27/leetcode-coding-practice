from collections import Counter
X = int(input())
N = map(int,input().split())
x = int(input())
L = map(tuple,(map(int,input().split()) for _ in range(x)))
n = Counter(N)
p =0
for i in L:
    if n[i[0]] > 0:
        n[i[0]] -= 1
        p += i[1]
print(p)
