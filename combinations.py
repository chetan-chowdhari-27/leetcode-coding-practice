# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inss_val, iterators = input().split()
inss_val = sorted(inss_val.upper())
# print(inss_val)
iterators = int(iterators)
# print(iterators)

for i in range(1,iterators+1):
    for item in combinations(inss_val, i):
        print(''.join(item))
