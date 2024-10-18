# Set .intersection() Operation
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8


a_index = int(input())
a_set = set(input().split())

b_index = int(input())
b_set = set(input().split())

set_intersection = len(a_set.intersection(b_set))
print(set_intersection)
