# ----------- Input --------------------
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# ----------- Output --------------------
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20


from collections import defaultdict

n = int(input())

dictionary_fruits_bc = {}

for _ in range(1,n+1):
    fruits_input = list(map(str, input().split()))
    quantities = int(fruits_input[-1])
    fruitsi = " ".join(fruits_input[:-1])
    # print(fruitsi)
    # print(quantities)

    if  fruitsi in dictionary_fruits_bc:
        dictionary_fruits_bc[fruitsi] += quantities
    else:
        dictionary_fruits_bc[fruitsi] = quantities


for i in dictionary_fruits_bc:    
    print(i, dictionary_fruits_bc[i])

