  # Finding the percentage
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

n = int(input('enter the array size of student :'))
dicts = {}
for i in range(n):
    names, *lines = input().split()
    # print(names, lines)
    scores = list(map(float, lines))
    dicts[names] = scores

query_name = input()
average_print = sum(dicts[query_name]) / len(dicts[query_name])
print(format(average_print, '.2f')) 




