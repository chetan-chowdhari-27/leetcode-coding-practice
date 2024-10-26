def inspusrs(N):
    new_lis = []
    inputss = []
    for _ in range(N):
        ins = input().split()
        if ins[0] == "append":
            try:
                inputss.append(int(ins[1]))
            except (IndexError, ValueError):
                continue  # Skips if there's an issue with input format

        elif ins[0] == "insert":
            try:
                inputss.insert(int(ins[1]), int(ins[2]))
            except (IndexError, ValueError):
                continue

        elif ins[0] == "remove":
            try:
                inputss.remove(int(ins[1]))
            except (ValueError, IndexError):
                continue  # Ignore if item not found or index issues

        elif ins[0] == "sort":
            inputss.sort()  # Sort in descending order

        elif ins[0] == "pop":
            if inputss:  # Only pop if list is not empty
                inputss.pop()
        elif ins[0] == "reverse":
            inputss.reverse()

        elif ins[0] == "print":
            new_lis.append(inputss[:])  # Append a copy of inputss to avoid future modifications


    for rg_in in new_lis:
        print(rg_in)  # Print each list in new_lis

    # return new_li



insps = int(input())
print(inspusrs(N=insps))
