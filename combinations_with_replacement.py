# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

insputs, iterations = input().split()
insputs = sorted(insputs.upper())
iterations = int(iterations)
# print(insputs)
# print(iterations)

combinations_with_replacements = list(combinations_with_replacement(insputs,iterations))
for i in combinations_with_replacements:
    print("".join(i))
