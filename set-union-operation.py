# Set .union() Operation
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8


a_index = int(input())
a_set = set(input().split())
# print(a_set)
b_index = int(input())
b_set = set(input().split())
# print(b_set)

set_union = len(a_set.union(b_set))
print(set_union)
