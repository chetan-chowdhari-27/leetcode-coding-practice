# Set .difference() Operation
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

english_newpaper = int(input())
english_newpaper_list  = set(map(int, input().split()))

french_newpaper = int(input())
french_newpaper_list  = set(map(int, input().split()))
sets_match = len(sorted(english_newpaper_list.difference(french_newpaper_list)))
print(sets_match)



