# Symmetric Difference

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}


# Enter your code here. Read input from STDIN. Print output to STDOUT

a_len = int(input())
a_list = set(input().split())

b_len = int(input())
b_list = set(input().split())

symmetric_difference_val = sorted(a_list.symmetric_difference(b_list), key=int)
for i in symmetric_difference_val:
    print(i)
