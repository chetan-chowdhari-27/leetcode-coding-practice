import numpy

n,m,p = list(map(int, input().split()))
# print(n)
# print(m)
# print(p)
new_list= []
for i in range((n+m)):
    new_lis = list(map(int, input().split()))
    new_list.append(new_lis)
new_list_np = numpy.array(new_list)
print(new_list_np)
