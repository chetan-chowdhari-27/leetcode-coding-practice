def split_and_join(line):
    # write your code here
    spliting = line.split(' ')
    merging = "-".join(spliting)
    return merging

if __name__ == '__main__':
    print(split_and_join('hello chetan'))
     