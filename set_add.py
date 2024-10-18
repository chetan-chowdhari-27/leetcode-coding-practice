# Enter your code here. Read input from STDIN. Print output to STDOUT


index_lst = int(input())

country_lst = set()
for i in range(1, index_lst):
    strings = input()
    country_lst.add(strings)

print(len(country_lst))
