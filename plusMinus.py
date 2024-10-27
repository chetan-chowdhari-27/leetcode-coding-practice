def plusMinus(arr):
    # Write your code here
    positive = []
    negative = []
    zero = []
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i< 0:
            negative.append(i)
        elif i == 0:
            zero.append(i)
    positive_sums = "{:.6f}".format(len(positive)/len(arr))
    negative_sums = "{:.6f}".format(len(negative)/len(arr))
    zero_sums = "{:.6f}".format(len(zero)/len(arr))

    print(positive_sums)
    print(negative_sums)
    print(zero_sums)
 
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
