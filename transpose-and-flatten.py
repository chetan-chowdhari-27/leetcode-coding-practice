import numpy

n,m= list(map(int, input().split()))
# print(n)
# print(m)
nre_list =[]
for i in range(n):
    ars = list(map(int,input().split()))
    nre_list.append(ars)
np_arr = numpy.array(nre_list)
# print(np_arr)
print(np_arr.transpose())
print(np_arr.flatten())
