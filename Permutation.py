from itertools import permutations

ins_per,itersa  = input().split()
# print(ins_per)
# print(itersa)
sorted_perma = sorted(permutations(ins_per, int(itersa)))
for i in list(sorted_perma): 
    print (''.join(i).upper()) 
